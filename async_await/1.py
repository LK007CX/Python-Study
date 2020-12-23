import time


def hello():
    time.sleep(1)
    print('Hello World:%s' % time.time())


def run():
    for i in range(5):
        hello()


if __name__ == "__main__":
    run()
