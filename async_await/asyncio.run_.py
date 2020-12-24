import asyncio
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(main())
# asyncio.run(main())


class Th(QThread):
    def __init__(self):
        super(Th, self).__init__()

    def run(self):
        while True:
            # print(time.strftime('%X'))
            # time.sleep(1)
            asyncio.run(main())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Th()
    t.start()
    sys.exit(app.exec_())