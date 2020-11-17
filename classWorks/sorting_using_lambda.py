#!usr/bin/env python3
l = [["Nawaraj",97],["David",92],["Manoj",94]]
# sort the list
l.sort()
#define a function to use as keywords in sort function
def sortfunc(x):
    return x[1]
#use this function to sort our list
l.sort(key=sortfunc)
l.sort(key=sortfunc, reverse=True)

# Use lambda function instead to sort the list
l.sort(key = lambda x: x[1])
l.sort(key = lambda x: x[1], reverse = True)
