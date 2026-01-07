if __name__ == '__main__':
    s1 = 'it is \time \to \read \now'
    s2 = r'\it \is \time \to \read \now'
    print(s1)
    print(s2)

    print(ord('a'))
    print(ord('A'))

    s1 = 'hello world'
    print('he' in s1)
    print('aa' not in s1)

    #切片
    g = 'helLo world'
    print(g[::1])
    print(g[::-1])

    print(g.upper())
    print(g.lower())
    print(g.capitalize())
    print(g.title())

    print(g.find('o'))

    print(f'{123:>10d}')
    print(f'{0.123:.2%}')

    #修剪
    str1 = '   ~~npc~~   '
    print(str1.strip())