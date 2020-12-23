# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 12:49
# @Author  : Lee
# @Email   : 1317108121@qq.com
# @File    : 5.py
# @Software: PyCharm


# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 12:21
# @Author  : Lee
# @Email   : 1317108121@qq.com
# @File    : 4.py
# @Software: PyCharm


import time
import asyncio
from aiohttp import ClientSession

tasks = []
url = "https://www.baidu.com"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            print('Hello World:%s' % time.time())

            return await response.read()


def run():
    loop = asyncio.get_event_loop()
    for i in range(5):
        task = asyncio.ensure_future(hello(url))
        tasks.append(task)
    results = loop.run_until_complete(asyncio.gather(*tasks))
    print(results)


if __name__ == '__main__':
    run()
