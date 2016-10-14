#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import asyncio
import pymysql


@asyncio.coroutine
def test_example():
    conn = yield from pymysql.connect(user='root',passwd = '123',db='test')

    cur = yield from conn.cursor()
    yield from cur.execute("SELECT user_id,User_name FROM blogs")
    print(cur.description)
    r = yield from cur.fetchall()
    print(r)
    yield from cur.close()
    conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_example())