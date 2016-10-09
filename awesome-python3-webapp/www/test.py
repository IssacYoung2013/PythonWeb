#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import orm 
import asyncio
from models import User,Blog,Comment

loop = asyncio.get_event_loop()

async def test():
	await orm.create_pool(loop,user='root',password='123',database='awesome')
	u = User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')
	await u.save()

test()
	