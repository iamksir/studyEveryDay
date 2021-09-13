items = list(map(lambda x: x ** 2, filter(lambda x:x % 2, range(1, 10))))
print(items)

items = [x ** 2 for x in range(1, 10) if x % 2]
print(items)

f = filter(lambda x:x % 2, range(1, 10))
items = list(f)
print(items)
