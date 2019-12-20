# 生成器适用：列表元素有生成规律
# # 列表生成式,创建generator,把[]改为() 
# L = [x*x for x in range(10)]
# print("列表",L)
# g = (x*x for x in range(10))
# print("生成器",g)
# # 遍历就是每次调用next(g)
# for n in g:
#     print(n)

# 函数生成generator,用yield关键字
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n = n + 1
#     return 'done'

# for n in fib(6):
#     print(n)

def triangles():
    l = [1]
    while True:
        yield l 
        # l = [l[i-1]+l[i] for i in rang(len(l))]
        list = []
        print("循环次数",range(len(l)))
        for i in range(len(l)):
            print("i:",i)
            print("11111",l[i-1])
            print("3333333",l[i])
            last = l[i-1] or 0
            cur = l[i] or 0
            print("last",last)
            print("cur",cur)
            list.append(last+cur)
        l = list

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 3:
        break

for t in results:
    print(t)