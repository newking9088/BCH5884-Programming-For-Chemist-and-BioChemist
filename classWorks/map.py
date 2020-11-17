#!usr/bin/env python3
# Define a function that always returns an even number
def even(x):
    if x%2 == 0:
        return x
    return x + 1
# Define a list
l = list(range(10))
# use map to convert all elements in a list to even elements
l1 = list(map(even,l))
l2 = tuple(map(even,l))
print(l1)
print(l2)
