#!usr/bin/env python3
x = 40

def f1():
    global x
    x = 88
    print(x)

def f2():
    global x
    x = 160
    print(x)

print(x)
f2()
f1()
f2()
print(x)


#################################
def positional(a,b,c):
    print(a,b,c)
def keyword(a=1,b=1,c=1):
    print(a,b,c)
# Always positional first and keyword second
def pos_and_key(a,b,c=1):
    print(a,b,c)
pos_and_key(2,3,5)
# *nums means arbitrary number of positional arguments
def mean(name,*nums):
    print( type(nums))
    if len(nums) == 0:
        return 0.0
    else:
        mean = sum(nums)/len(nums)
    print(name, mean)
    return mean

#mean("Nawaraj", 90,98,97,99,78)

def grades(course, **gradebook):
    print(type(gradebook))
    print(gradebook)
    for key in gradebook.keys():
        mean = sum(gradebook[key]/len(gradebook[key])
    print(course, key, mean)


                   
