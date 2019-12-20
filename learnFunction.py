#!/user/local/bin/python3
# 参数可组合,顺序必须是：必选参数，默认参数，可变参数，命名关键字参数，关键字参数
# 默认参数，必须指向不变对象
def add_end(L=[]):
    L.append('End')
    return L
print(add_end())
print(add_end())
# ['End']
# ['End', 'End']
# 出错原因：函数在定义时，默认参数已被创建

# 可变参数:*修饰,类似lua...,在函数调用是自动把多个参数组装成一个tuple
def calc(*args):
    print(args)
calc()
calc(1,2)
nums = [1,2,3]
# ([1, 2, 3],)
calc(nums)
# (1, 2, 3)
calc(*nums)

#关键字参数:**修饰，关键字参数自动组装成一个dict
def person(name,age,**kw):
    print("name:",name,"age:",age,"other",kw)
person('siho',14)
person('momo',13,city='tokyo',job='student')
extra = {'city':'beijing','job':'engineer'}
person("link",29,**extra)

# 命名关键字参数,必须传值，否则会报错
def student(name,age,*,grade):
    print("name:",name,"age:",age,"grade",grade)
student("lily",13,grade=6)
