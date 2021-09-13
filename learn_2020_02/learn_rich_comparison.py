from enum import Enum, unique

@unique
class Suite(Enum):
    '''花色'''
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value

S1 = Suite(1)
S2 = Suite(2)
print(f'{S1.name}:{S1.value}')
print(f'{S2.name}:{S2.value}')
print(S1 == S2)
print(S1 < S2)