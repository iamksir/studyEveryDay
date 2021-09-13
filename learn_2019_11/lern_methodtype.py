class Student(object):
    pass

#给实例绑定属性
s = Student()
s.name = 'Joker'
print(s.name)

#给实例绑定方法
def set_age(self,age):
    self.age = age

from types import MethodType
s3 = Student()
s4 = Student()
s3.set_age = MethodType(set_age,s3) #绑定set_age到s
s3.set_age(18)
print(s3.age)
#print(s4.set_age) #AttributeError: 'Student' object has no attribute 'set_age'

#给类绑定方法
def set_sex(self,sex):
    self.sex = sex

from types import MethodType
s1 = Student()
s2 = Student()
Student.set_sex = MethodType(set_sex,Student)
s1.sex = '男'
s2.set_sex('女')
print(s1.sex,s2.sex)



