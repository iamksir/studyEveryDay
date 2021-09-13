class A(object):
    def fun(self):
        print('A.fun')

class B(object):
    def fun(self):
        print('B.fun')

class C(object):
    def fun(self):
        print('C.fun')

class D(A, B):
    def fun(self):
        print('D.fun')

class E(B, C):
    def fun(self):
        print('E.fun')

class F(D, E):
    def fun(self):
        print('F.fun')

super(E, F()).fun()
super(D, F()).fun()
super(F, F()).fun()
super(B, F()).fun()
super(B, E()).fun()
#super(B, B()).fun() #AttributeError: 'super' object has no attribute 'fun'

print(super(F, F()).fun) #<bound method D.fun of <__main__.F object at 0x0000022AC4395D30>>
print(super(F, F).fun) #<function D.fun at 0x0000022AC4394EA0>
print(D.fun)           #<function D.fun at 0x0000022AC4394EA0>
print(super(D, F).fun) #<function A.fun at 0x00000262EE154A60>
print(super(F, F).fun(F()))