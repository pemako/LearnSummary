#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""mysql连接池

本模块提供了一组全局的mysql连接池，可以在一个py文件中import本模块并初始化，
在其他的py文件import本模块，对数据库进行访问。

import mysql_util as MU
MU.registerConnection('online_db', host="", port=3306,
	user='', passwd='', db='online_db', pool_size=8)

id = 1
name = "中文或者%s;'; DELETE FROM t1; 等特殊符号"
sql = 'SELECT * FROM t1 WHERE id=%s OR name=%s'
params = (id, name)
rows = MU.fetchall('online_db', sql, params)

本模块适合用于一些简单的任务型程序，与dbtypes配合使用。对于可靠性要求更高的服
务，建议使用django
"""

import time
import MySQLdb
from MySQLdb import OperationalError
import threading
import logging
import logging.config

_conn_map = {}

_logger = logging.getLogger('mysql_util')


class MySQLConnPool(object):
    def __init__(self, host, port, user, passwd, db, pool_size=8):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.pool_size = pool_size

        self.__connections = []
        self.__conn_num = 0
        self.__conn_cond = threading.Condition()

    def getConn(self):
        self.__conn_cond.acquire()
        while len(self.__connections) == 0 and self.__conn_num >= self.pool_size:
            self.__conn_cond.wait(1)
        try:
            if len(self.__connections) == 0:
                conn = MySQLdb.connect(host=self.host,
                                       port=self.port,
                                       user=self.user,
                                       passwd=self.passwd,
                                       db=self.db,
                                       charset='UTF8')
                self.__conn_num += 1
                conn.autocommit(True)
            else:
                conn = self.__connections.pop(0)
        except Exception, e:
            _logger.error(e)
            conn = None

        self.__conn_cond.release()
        return conn

    def releaseConn(self, conn):
        self.__conn_cond.acquire()
        self.__connections.append(conn)
        self.__conn_cond.notify()
        self.__conn_cond.release()

    def closeConn(self, conn):
        try:
            conn.close()
        except:
            pass

        self.__conn_cond.acquire()
        self.__conn_num -= 1
        self.__conn_cond.notify()
        self.__conn_cond.release()


def registerConnection(key, host, port, user, passwd, db, pool_size=4):
    _conn_map[key] = MySQLConnPool(host, port, user, passwd, db, pool_size)


def getConnection(key):
    return _conn_map[key].getConn()


def releaseConnection(key, conn):
    _conn_map[key].releaseConn(conn)


def closeConnection(key, conn):
    _conn_map[key].closeConn(conn)


class AutoCall:
    def __init__(self, key, conn, fun):
        self.key = key
        self.conn = conn
        self.fun = fun

    def __del__(self):
        self.fun(self.key, self.conn)


def query(key, sql, parameters=None):
    _conn = getConnection(key)
    _cursor = _conn.cursor()
    if parameters:
        dp = []
        if isinstance(parameters, list) or isinstance(parameters, tuple):
            for v in parameters:
                if (isinstance(v, str) or isinstance(v, unicode)) and len(v) > 256:
                    dp.append(v[0:253] + '...len:%d' % len(v))
                else:
                    dp.append(v)
        else:
            dp = parameters
        _logger.debug(sql % _conn.literal(dp))
    else:
        _logger.debug(sql)

    try:
        _cursor.execute(sql, parameters)
        return _conn, _cursor
    except OperationalError, oe:  # maybe timeout, retry once
        _logger.warn("%s, retry once", oe)
        try:
            _cursor.close()
        except:
            pass
        closeConnection(key, _conn)
        _conn = getConnection(key)
        try:
            _cursor = _conn.cursor()
            _cursor.execute(sql, parameters)
        except Exception, e:
            _logger.error(e)
    except Exception, e:
        _logger.error(e)

    return _conn, _cursor


def fetchone(key, sql, parameters=None):
    _conn, _cursor = query(key, sql, parameters)
    _row = _cursor.fetchone()
    _cursor.close()
    releaseConnection(key, _conn)
    return _row


def fetchall(key, sql, parameters=None):
    _conn, _cursor = query(key, sql, parameters)
    ac = AutoCall(key, _conn, releaseConnection)
    ret = []
    _row = _cursor.fetchone()
    while _row:
        ret.append(_row)
        _row = _cursor.fetchone()
    _cursor.close()
    return ret


def execute(key, sql, parameters=None):
    _conn, _cursor = query(key, sql, parameters)
    lastrowid = _cursor.lastrowid
    try:
        _cursor.close()
    except:
        pass
    releaseConnection(key, _conn)
    return lastrowid

# transaction related functions


def begin_t(key):
    _conn = getConnection(key)
    _conn.begin()
    return _conn


def rollback_t(key, _conn):
    _conn.rollback()
    releaseConnection(key, _conn)


def commit_t(key, _conn):
    _conn.commit()
    releaseConnection(key, _conn)


def query_t(_conn, sql, parameters=None):
    _cursor = _conn.cursor()
    _cursor.execute(sql, parameters)
    return _cursor


def fetchone_t(_conn, sql, parameters=None):
    _res = query_t(_conn, sql, parameters)
    _row = _res.fetchone()
    _res.close()
    return _row


def fetchall_t(_conn, sql, parameters=None):
    _res = query_t(_conn, sql, parameters)
    ret = []
    _row = _res.fetchone()
    while _row:
        ret.append(_row)
        _row = _res.fetchone()
    _res.close()
    return ret


def execute_t(_conn, sql, parameters=None):
    _cursor = query_t(_conn, sql, parameters)
    try:
        _cursor.close()
    except:
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    registerConnection('test', 'localhost', 3306, 'root', 'test', 'pemako')
    print fetchall('test', 'show tables')
    tables = fetchall('test', 'show tables like %s', ('%a%',))
    print tables
    if tables:
        t = tables[0]
        print fetchall('test', 'SELECT * FROM %s LIMIT %%s' % t, (1))
    long_str = 'xx'.join(['y' for i in range(200)])
    tables = fetchall('test', 'show tables like %s', (long_str,))
