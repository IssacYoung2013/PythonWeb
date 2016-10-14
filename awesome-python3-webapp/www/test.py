#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import orm 
import asyncio
from models import User,Blog,Comment

async def test():
	await orm.create_pool(user='root',passwd='123',db='awesome')
	u = User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')
	print('===debug===')
	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())