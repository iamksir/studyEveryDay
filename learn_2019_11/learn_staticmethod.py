from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod #静态方法
    def is_valid(a, b, c): #没有默认参数self
        return a + b > c and a + c >b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

if __name__ == "__main__":
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(Triangle.perimeter(t))
        print(t.area())
        print(Triangle.area(t))
    else:
        print('无法构成三角形')