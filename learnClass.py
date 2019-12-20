# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
    
#     def print_score(self):
        # print("%s:%s" % (self.__name,self.__score))
    
#     def get_name(self):
#         return self.__name
   

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# print("======",lisa.get_name())
# print(dir(bart))

# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# class Student(object):
#     pass
# s = Student()
# s.name = "s"
# def set_age(self,age):
#     self.age = age
# from types import MethodType
# # 给实例动态绑定方法，仅绑定的实例可以调用该方法
# # s.set_age = MethodType(set_age,s)
# # 给类动态绑定方法
# Student.set_age = set_age
# s.set_age(25)
# print('s age:%d' %s.age)
# s1 = Student()
# # s1.set_age(25) 报错

# class Screen(object):

#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self,value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,value):
#         self._height = value

#     @property
#     def resolution(self):
#         return  self._width*self._height

# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# s.resolution = 100
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

