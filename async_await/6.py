# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 12:51
# @Author  : Lee
# @Email   : 1317108121@qq.com
# @File    : 6.py
# @Software: PyCharm
import asyncio
import time

from aiohttp import ClientSession

url = "https://www.baidu.com"


async def hello(url, semaphone):
    async with semaphone:
        async with ClientSession() as session:
            async with session.get(url) as response:
                return await response.read()


async def run():
    semahore = asyncio.Semaphore(500)  # 限制并发量为500
    to_get = [hello(url, semahore) for i in range(500)]
    await asyncio.wait(to_get)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
