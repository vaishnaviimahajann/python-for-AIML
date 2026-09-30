#collection of unique elements sets are mutable
set={2,34,56,43,65,33}
print(set)
print(type(set))
print(len(set))

set.add(67)
set.add(34)
set.add(4566)
print(set)
set.remove(56)
print(set)
set.pop()
print(set)