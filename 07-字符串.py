if __name__ == '__main__':
    s1 = 'hello world'
    print(len(s1))
    for i in range(len(s1)):
        print(s1[i], end='')
    for e in s1:
        print(e, end='')
    print('\n')

    print(s1.startswith('hello'))
    print(s1.isdigit())
    print(s1.isalpha())

    #打印
    print(s1.center(20, '*'))
    print(s1.rjust(20, '*'))
    print(s1.ljust(20, '*'))

    #替换
    print(s1.replace('l', '*', 2))

    #拆分合并
    s = 'I love you'
    print(s.split(' '))
    print('!'.join(s.split(' ')))