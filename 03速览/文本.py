print('single line')
print('''\
multiple line
multiple line
multiple line
''')

#索引
s = 'hello'
print(s[-1])
print(s[4])

#切片 [)
s = 'world'
print(s[1:])
print(s[:-1])
print(s[:2], s[2:])

# print(s[10]) # error
print(s[10:11] + 'a') #不会报错，切片会自动处理

print(len(s))