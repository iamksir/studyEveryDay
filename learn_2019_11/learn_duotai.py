class Pet(object):

    def __init__(self, name):
        self._name = name

    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print('%s：汪汪汪...' %self._name)

class Cat(Pet):
    def make_voice(self):
        print(('%s：喵..喵..' %self._name))

if __name__ == "__main__":
    pets = [Dog('旺财'),Cat('加菲'),Dog('大黄')]
    for pet in pets:
        pet.make_voice()

