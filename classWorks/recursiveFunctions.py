#!usr/bin/env python3
times = lambda x,y: x**y
def exp(x,y):
    return x**y
l =[lambda x:x**2, lambda x:x**3, lambda x: x**4]

def power(x,n):
    if n == 0:
        return 1
    elif n > 0:
        return x*power(x,n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


