from functools import reduce
# def normalize(name):
#     return name[0].upper()+name[1:].lower()
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# def prod(L):
#     return reduce(lambda a,b:a*b,L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2num(s):
#     return DIGITS[s]
# def str2int(s):
#     return reduce(lambda a,b:a*10+b,map(char2num,s))
# def str2float(s):
#     flist = s.split('.')
#     return str2int(flist[0])+str2int(flist[1])/(10**len(flist[1]))
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def is_palindrome(n):
#     string = str(n)
#     lenght = len(string)
#     s,e = 0,-1
#     while s <= lenght/2:
#         if string[s] != string[e]:
#             return False
#         s += 1
#         e -= 1
#     return True

# # 测试:
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

def createCounter():
    def counter():
        num = 0
        while True:
            num += 1
            yield num
    c = counter()
    def myNext():
        return next(c)
    return myNext
# 测试:
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')