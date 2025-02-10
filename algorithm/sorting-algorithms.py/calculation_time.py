import time
import random
def cal_time(func):#定义一个计时器，传入一个函数，并返回另一个附加了计时功能的方法
    def wrapper(*args, **kwargs):#定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper # 将包装后的函数返回