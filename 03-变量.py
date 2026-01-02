import math

if __name__ == '__main__':
    # 整型
    print(0b11)
    print(0o11)
    print(11)
    print(0x11)

    #浮点型
    print(12.23)
    print(1.22e6)

    #字符串
    print("hello python")

    #bool
    print(True)
    print(False)

    #类型
    a = 10
    b = 20.2
    c = "hello python"
    print(type(a))
    print(type(b))
    print(type(c))

    #类型转换
    a = 100
    b = 123.45
    c = '123'
    d = '100'
    e = '123.45'
    f = 'hello, world'
    g = True
    print(float(a))  # int类型的100转成float，输出100.0
    print(int(b))  # float类型的123.45转成int，输出123
    print(int(c))  # str类型的'123'转成int，输出123
    print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
    print(int(d, base=2))  # str类型的'100'按二进制转成int，输出4
    print(float(e))  # str类型的'123.45'转成float，输出123.45
    print(bool(f))  # str类型的'hello, world'转成bool，输出True
    print(int(g))  # bool类型的True转成int，输出1
    print(chr(a))  # int类型的100转成str，输出'd'
    print(ord('d'))  # str类型的'd'转成int，输出100
    print(int(True))
    print(int(False))

    #运算
    a = 10
    b = 3
    a += b  # 相当于：a = a + b
    a *= a + 2  # 相当于：a = a * (a + 2)
    print(a)  # 大家算一下这里会输出什么

    print((a := 10))

    # f = float(input('请输入华氏温度'))
    # c = (f - 32) / 1.8
    # print('%.1f华氏温度=%.1f摄氏度' % (f, c))
    # print(f'{f:.2f}华氏温度={c:.1f}摄氏温度')

    radis = float(input('请输入圆的半径：'))
    perimeter = 2 * math.pi * radis
    area = math.pi * radis ** 2
    print('圆的周长: %.2f' % perimeter)
    print(f'圆的面积: {area:.2f}')