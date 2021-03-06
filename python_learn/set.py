# -*- coding:utf-8 -*-

a = {1, 2, 3, 4, 5}
print(a)

b = [1, 2, 3, 4, 5, 6]
c = set(b)
print(c)

# no repeatable items
d = {1, 1, 1, 2, 2, 2, 3, 3, 3,}
print(d)

# bool
print(1 in a)

# add()
a.add("string")
a.add((10, 11))
print(a)

# update()
a.update([12, 13])
print(a)

# remove()
a.remove(13)
print(a)
a.discard(12)
print(a)
g = {111, 222, 333}
print(g)
print(g.clear())

# union()
e = {3, 4, 5}
f = {11, 22, 33}
print(e.union(f))

# intersection()
print(e.intersection(f))

# issubset()
print(e.issubset(a))

# issuperset()
print(a.issuperset(e))



