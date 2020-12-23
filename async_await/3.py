# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 12:14
# @Author  : Lee
# @Email   : 1317108121@qq.com
# @File    : 3.py
# @Software: PyCharm


import asyncio
from aiohttp import ClientSession

tasks = []
url = "https://www.baidu.com/"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))
