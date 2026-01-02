import random
import time

if __name__ == '__main__':
    height = 168
    weight = 70
    bmi = weight / (height/100) ** 2
    print(f'bmi is {bmi :.2f}')
    if 12 < bmi < 18.5:
        print('perfect')
    elif bmi < 25:
        print('just so so')
    else:
        print('too fat')


    status_code = 401
    match status_code:
        case 200 | 202: desc = 'ok'
        case 400: desc = 'bad request'
        case 404: desc = 'not found'
        case _: desc = 'unknown'
    print('status is', desc)


    x = 100
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print(f'y = {y}')

    # for
    # for i in range(1, 5):
    #     print(f'hello {i}')
    #     time.sleep(1)

    # total = 0
    # for i in range(0, 101, 10):
    #     total += i
    #     print(f'i = {i}')
    # print(f'total = {total}')
    #
    # print(f'total: {sum(range(0, 11, 2))}')

    # total = 0
    # while True:
    #     total += 1
    #     if total > 100:
    #         break
    # print(total)

    # answer = random.randrange(1, 101)
    # counter = 0
    # while True:
    #     counter += 1
    #     num = int(input('请输入：'))
    #     if num < answer:
    #         print('小了')
    #     elif num > answer:
    #         print('大了')
    #     else:
    #         print('猜对了')
    #         break

    """
    输出素数
    """
    for num in range(2, 100):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f'{num} is prime')


    """
    斐波那契数列
    """
    print('-------------------斐波那契数列')
    a, b = 0, 1
    for _ in range(10):
        a, b = b, a + b
        print(a)

    """
    水仙花数
    """
    print('-------------------水仙花数')
    for i in range(100, 1000):
        x = i // 100
        y = (i - x * 100) // 10
        z = (i - x * 100 - y * 10)
        if x ** 3 + y ** 3 + z ** 3 == i:
            print(f'{i} 是水仙花数')

    """
    百钱买百鸡
    """
    print('-------------------百钱买百鸡')
    for x in range(0, 21):
        for y in range(0, 34):
            z = 100 - x - y
            if z % 3 == 0 and (x * 5 + y * 3 + z // 3 == 100):
                print(f'公鸡{x} 母鸡{y} 小鸡{z}')