import itertools

l = itertools.permutations('ABCD', 4)
print(list(l))

l = itertools.combinations('ABCD', 3)
print(list(l))

l = itertools.product('ABCD', '1234')
print(list(l))

l = itertools.count(10, 2)
print(list(itertools.islice(l,5)))

l = itertools.cycle('xyz')
print(list(itertools.islice(l,5)))


