#!/usr/bin/env python
# -*- coding: utf-8

"""python的多线程，无法利用多个cpu core，在多进程时，logging如果写一个文件，
无法保证日志逐条写入，切分日志时，如果一个进程做了切分，会导致其他进程无法
正常写入。

在多进程模式下，可以在主进程开启一个socket server，接受来自若干子进程的日志
请求，并将其写入文件，以避免上述问题。

在主进程中，可以执行如下的代码，开启一个独立的线程，用于日志收集

from loggingext.sockethanlder import LogRecordSocketReceiver

def runLogReceiverThread(self):
    #启动一个独立的线程，收集worker的日志
    tcpserver = LogRecordSocketReceiver('localhost', 
        self.cfg.getint('default', 'logging.port'))
    t = threading.Thread(target=tcpserver.serve_until_stopped)
    t.daemon = True
    t.start()

在子进程中，一启动子进程后，就重新初始化logging机制，使用这个socketserver，可以
参考本模块下的 logging-worker.conf

def resetWorkerLogConfig(self):
    #重置worker的logging config
    logging.config.fileConfig(
    	os.path.join(self.executeDir, 'conf/logging-worker.conf'))
这个代码是从如下地址复制的
http://docs.python.org/2/howto/logging-cookbook.html#sending-and-receiving-logging-events-across-a-network
"""

import logging
import logging.handlers
import pickle
import SocketServer
import struct


class LogRecordStreamHandler(SocketServer.StreamRequestHandler):
    """Handler for a streaming logging request.

    This basically logs the record using whatever logging policy is
    configured locally.
    """

    def handle(self):
        """
        Handle multiple requests - each expected to be a 4-byte length,
        followed by the LogRecord in pickle format. Logs the record
        according to whatever policy is configured locally.
        """
        while True:
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.connection.recv(slen - len(chunk))
            obj = self.unpickle(chunk)
            record = logging.makeLogRecord(obj)
            self.handle_log_record(record)

    def unpickle(self, data):
        return pickle.loads(data)

    def handle_log_record(self, record):
        # if a name is specified, we use the named logger rather than the one
        # implied by the record.
        if self.server.logname is not None:
            name = self.server.logname
        else:
            name = record.name
        logger = logging.getLogger(name)
        # N.B. EVERY record gets logged. This is because Logger.handle
        # is normally called AFTER logger-level filtering. If you want
        # to do filtering, do it at the client end to save wasting
        # cycles and network bandwidth!
        logger.handle(record)


class LogRecordSocketReceiver(SocketServer.ThreadingTCPServer):
    """
    Simple TCP socket-based logging receiver suitable for testing.
    """

    allow_reuse_address = 1

    def __init__(self, host='localhost',
                 port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
                 handler=LogRecordStreamHandler):
        SocketServer.ThreadingTCPServer.__init__(self, (host, port), handler)
        self.abort = 0
        self.timeout = 1
        self.logname = None

    def serve_until_stopped(self):
        import select
        abort = 0
        while not abort:
            rd, wr, ex = select.select([self.socket.fileno()],
                                       [], [],
                                       self.timeout)
            if rd:
                self.handle_request()
            abort = self.abort


def main():
    # logging.basicConfig(format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
    tcpserver = LogRecordSocketReceiver()
    # print('About to start TCP server...')
    tcpserver.serve_until_stopped()


if __name__ == '__main__':
    main()
