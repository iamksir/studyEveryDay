class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def name(self):
        return self._name

    def play(self):
        print('%s正在玩耍。' % self._name)

    def watch_tv(self):
        if self._age >= 18:
            print('%s正在玩电脑。' % self._name)
        else:
            print('%s正在看动画片、' % self._name)


class Student(Person):

    def __init__(self,name,age,grade):
        # super()首先找到父类，然后把Student的对象转换为父类的对象
        super(Student, self).__init__(name, age)
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s。' %(self._grade, self._name, course))

class Teacher(Person):

    def __init__(self,name,age,title):
        super().__init__(name, age)
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s。'%(self._name, self._title, course))


if __name__ == "__main__":
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_tv()
    t = Teacher('Joker', 25, '叫兽')
    t.teach('Python')
    t.watch_tv()