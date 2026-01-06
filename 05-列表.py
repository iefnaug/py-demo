if __name__ == '__main__':
    # items1 = [35, 12, 99, 68, 55, 35, 87]
    # items2 = ['Python', 'Java', 'Go', 'Kotlin']
    # items3 = [100, 12.3, 'Python', True]
    # print(items1)  # [35, 12, 99, 68, 55, 35, 87]
    # print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
    # print(items3)  # [100, 12.3, 'Python', True]
    # print(type(items1))
    #
    # items4 = list(range(10))
    # items5 = list('hello')
    # print(items4)
    # print(items5)
    # print(items1 + items2)
    # items1 += items2
    # print(items1)
    # print(items1 * 2)
    #
    # if 35 in items1:
    #     print(f'35 in {items1}')
    # if 3 not in items1:
    #     print(f'3 not in {items1}')
    #
    # item0 = list(range(10))
    # print(item0[-1], item0[-10])
    # print(item0[0:5:2])
    # print(item0[-1:-10:-2])
    # print(item0[-2::-1])
    # print(item0[:5:1])
    # print(item0[:-5:-1])
    #
    # item0[1:5:2] = [11, 33]
    # print(item0)
    #
    # for index in range(len(item0)):
    #     print(item0[index])
    # for item in item0:
    #     print(item)

    # 增删
    # languages = ['Python', 'Java', 'Java', 'C++']
    # languages.append('JavaScript')
    # languages.insert(1, "SQL")
    # print(languages)
    # languages.remove("Java")
    # print(languages)
    # languages.pop()
    # print(languages)
    # languages.pop(0)
    # print(languages)
    # del languages[0]
    # print(languages)
    # languages.clear()
    # print(languages)

    print('-------------------------------------常用方法|')
    # items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
    # print(items.index('Python'))
    # print(items.index('Python', 2))
    # print(items.count('Python'))
    # print(items.index('Python', 6))

    # items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
    # items.sort()
    # print(items)
    # items.reverse()
    # print(items)

    nums1 = [35, 12, 97, 64, 55]
    nums2 = []
    for num in nums1:
        nums2.append(num ** 2)
    print(nums2)
    nums3 = [num ** 2 for num in nums1]
    print(nums3)