from enum import Enum, unique

@unique
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
print(Color['red'])
print(Color(2))
red_member = Color.red
print(red_member.name)
print(red_member.value)

#遍历
for color in Color:
    print(color)

#同一性比较
print(Color.red is Color.red)
print(Color.red is Color.orange)
print(Color.red is not Color.blue)
#等值比较
print(Color.red == Color.purple)
print(Color.blue != Color.purple)