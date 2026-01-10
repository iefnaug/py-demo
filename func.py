import functools
import operator
import time
import random
import string

ALL_CHARS = string.ascii_letters + string.digits

def generate_code(*, code_len=4):
    # print(ALL_CHARS)
    return ''.join(random.choices(ALL_CHARS, k=code_len))

def is_prime(num: int=10) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def record_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'start={start}')
        result = func(*args, **kwargs)
        end = time.time()
        print(f'end={end}')
        print(f'{func.__name__}执行时间：{end - start:.2f}s')
        return result
    return wrapper

def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')




def add(a, b):
    return a + b

def demo(a, b, c, /):
    return a + b + c

def demo2(* , a, b, c):
    return a + b + c

def demo3(a, /, *, b):
    return a + b

def demo4(a, b=1):
    return a + b

def demo5(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    for k in kwargs:
        print(f'k={k}, v={kwargs.get(k)}', end=' ')

def demo6():
    old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
    new_strings = sorted(old_strings, key=len, reverse=True)
    print(new_strings)

def demo7():
    old_nums = [35, 12, 8, 99, 60, 52]
    new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
    print(new_nums)

def demo8():
    fac = lambda  n: functools.reduce(operator.mul, range(2, n + 1), 1)
    print(fac(4))

def demo9():
    """
    偏函数
    :return:
    """
    int2 = functools.partial(int, base=2)
    int16 = functools.partial(int, base=16)
    print(int('1001'))
    print(int2('1001'))
    print(int16('1001'))

if __name__ == '__main__':
    # print(add(b=1, a=2))
    # demo(1, 2, 3)
    # demo2(a=1, b=2, c=3)
    # demo3(1, b=2)
    # demo4(1, b=2)
    # demo5(1, a=1, b=2, c=3)
    # demo7()
    # demo8()
    # demo9()
    # record_time(download)('file')
    # upload('excel')
    # 取消装饰器
    upload.__wrapped__('mastering python')



