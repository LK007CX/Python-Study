import time
import asyncio


# 定义异步函数
async def hello():
    asyncio.sleep(1)
    print('Hello World:%s' % time.time())


def run():
    loop = asyncio.get_event_loop()
    for i in range(5):
        loop.run_until_complete(hello())


if __name__ == '__main__':
    run()
