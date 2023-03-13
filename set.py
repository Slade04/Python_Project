# Generation
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,5,4,3,2,1} # The same element will be reduced as one
set3=set(['dog','cat','chick','duck','tortoise'])
set4=frozenset([True,False])

# Access
print(set1)
for i in set1:
    print(i)

# Update
set2.update({6,7,8}) # Multiple elements
set2.add(9) # Single element
print(set2)
set2.remove(9)
try:
    set2.remove(10)
except KeyError:
    print('Element doesn\'t exist.')
print(set2)
set2.discard(8)
set2.discard(9)
print(set2)
set2.pop()
print(set2)

try:set4.clear()
except AttributeError:print('A frozenset cannot be updated,only accessed.')
print(set4)

# Calculation
print(1 in set1,12 in set1)
print(set1==set2,set3!=set4,set1>set2)
print(set1&set2,set2|set3,set2-set3,set1^set2)
