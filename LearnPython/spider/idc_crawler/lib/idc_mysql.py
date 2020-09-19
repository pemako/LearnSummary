# -*- coding: utf-8 -*-

"""
该文件用于数据访问的封装

使用MySQLdb

关于连接使用思考：
使用长连接优点是可重复使用该连接，避免经常建立连接
缺点是需要对连接进行保护，避免公用和并发，每次访问是还需要对是否超时进行判断或异常处理
短连接优点是每次连接不用考虑其他连接影响，减少异常思考
缺点是频繁的连接，可能会造成资源浪费
"""
import logging

import MySQLdb


class MySql:
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.logger = logging.getLogger('domino.mysql')

    def getConn(self):
        try:
            conn = MySQLdb.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.passwd,
                                   db=self.db,
                                   charset='UTF8')
        except Exception, e:
            raise Exception('%s. can not connect to mysql server' % (e))
        return conn

    def _execute(self, sql, parameters=None):
        conn = self.getConn()
        conn.autocommit(True)
        cursor = conn.cursor()
        if parameters:
            self.logger.debug(sql % conn.literal(parameters))
        else:
            self.logger.debug(sql)
        cursor.execute(sql, parameters)
        return conn, cursor

    def _encode_row(self, row):
        if not row:
            return row
        _row = list(row)
        for i in range(len(_row)):
            if isinstance(_row[i], unicode):
                _row[i] = _row[i].encode('utf-8')
        return tuple(_row)

    def fetchone(self, sql, parameters=None):
        conn, cursor = self._execute(sql, parameters)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return self._encode_row(row)

    def fetchall(self, sql, parameters=None):
        conn, cursor = self._execute(sql, parameters)
        rows = []
        results = cursor.fetchall()
        for row in results:
            rows.append(self._encode_row(row))
        cursor.close()
        conn.close()
        return rows

    def execute(self, sql, parameters=None):
        conn, cursor = self._execute(sql, parameters)
        cursor.close()
        conn.close()

    # transaction related functions
    def begin_t(self):
        conn = self.getConn()
        conn.begin()
        return conn

    def _execute_t(self, conn, sql, parameters=None):
        cursor = conn.cursor()
        cursor.execute(sql, parameters)
        return cursor

    def fetchone_t(self, conn, sql):
        cursor = self._execute_t(conn, sql, parameters=None)
        row = cursor.fetchone()
        cursor.close()
        return self._encode_row(row)

    def fetchall_t(self, conn, sql, parameters=None):
        cursor = self._execute_t(conn, sql, parameters)
        rows = []
        results = cursor.fetchall()
        for row in results:
            rows.append(self._encode_row(row))
        cursor.close()
        return rows

    def execute_t(self, conn, sql, parameters=None):
        cursor = self._execute_t(conn, sql, parameters)
        cursor.close()

    def rollback_t(self, conn):
        conn.rollback()
        conn.close()

    def commit_t(self, conn):
        conn.commit()
        conn.close()
