if __name__ == '__main__':
    dt = dict(zip('123', '456'))
    print(dt)
    print(dt.get('1'))
    print(dt['1'])
    print(dt.get('4'))
    # dt.popitem('4')
    dt.clear()
    print(dt)