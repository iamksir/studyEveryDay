class Person(object):
    __slots__ =  ('_name','_age','_gender')
    def __init__(self, name, age,):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 18:
            print('%s正在玩飞行棋' %self._name)
        else:
            print('%s正在玩斗地主' %self._name)

if __name__ == "__main__":
    person = Person('Bob', 12 )
    person._gender = '女'
    person.play()
    person._name = 'joker'
    person._age = 23
    person._gender = '男'
    #person.grade = 'A' #AttributeError: 'Person' object has no attribute 'grade'
    person.play()