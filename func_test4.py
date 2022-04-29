import time


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("函数运行了 %s 秒" % (stop_time - start_time))
    return wrapper


@timer
def i_can_sleep():
    time.sleep(3)


i_can_sleep()
