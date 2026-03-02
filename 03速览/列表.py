squares = [1,2,3,4,5,6]
#索引 + 切片
print(squares[1])
print(squares[-1])
# print(squares[11]) #报错
print(squares[11:12])

#合并
squares += [1,2,3,4,5,6]
print(squares)

#追加
squares.append(100)
print(squares)
squares[12] = 200
print(squares)

#切片浅拷贝
nums = [1,2,3,4,5,6]
nums2 = nums[:]
nums2[0] = 100
print(nums)
print(nums2)

#改变列表
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)


a, b = 1, 2
a, b = b, a + b

print(a, b)
