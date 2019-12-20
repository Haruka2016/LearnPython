#!/user/local/bin/python3

# 条件语句
# if 0:
#     print("0 is true")
# else:
#     print("0 is false")
# a = 9
# if a < 0 :
#     print("a < 0")
# elif a < 10 :
#     print("a < 10")

# 循环语句
# for letter in 'Python':
#     print('当前的字母：',letter)

# fruits = ['banana','apple','mango']
# for fruit in fruits:
#     print("1.当前的水果：",fruit)

# for index in range(len(fruits)):
#     print("2.当前的水果：",fruits[index])
#     # if fruits[index] == 'apple': break
# else:
#     print("2.循环正常结束,会触发else.")

# while len(fruits) > 0:
#     f = fruits.pop()
#     print("3.当前的水果：",f)
# else:
#     print("3.循环正常结束,会触发else.")

# 数据类型：

# 1.数字：整型，长整型，浮点型，复数

# 2.字符串
# print("hello world!")
# print("hello world!" + "你好 世界!")
# s = '012345'
# print("字符串截取s[0:6]",s[0:6])
# print("字符串截取s[-1]",s[-1])
# print("字符串截取s[0:-1]",s[0:-1])
# print("3 in s:","3" in s)
# print("My name is {} and weight is {} kg!".format('zara',21))
# print("My name is {name} and weight is {weight} kg!".format(name = 'lily',weight = 30))

# 3.列表[]
# list1 = 
# 4.元组()
# 5.字典{}
# my_d = {"pyon":91,"kraz":93,"mocho":92}
# name = my_d.pop("mocho")
# print(name)

# 函数
def test(*l):
    l = l or []
    l.append('END')
    return l
print(test())
print(test())

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum
