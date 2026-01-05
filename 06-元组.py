import timeit

def m1():
    # 定义一个三元组
    t1 = (35, 12, 98)
    # 定义一个四元组
    t2 = ('骆昊', 45, True, '四川成都')
    print(t2[1:3:2])

    a = 1,2,3,4,5
    b,c,*d = a
    print(b,c,d)

    print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
    print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

if __name__ == '__main__':
    m1()