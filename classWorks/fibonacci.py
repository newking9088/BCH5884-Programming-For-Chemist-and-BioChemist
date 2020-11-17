#!usr/bin/env python3
#Fibonacci Sequence:0,1,1,2,3,5,8,..............................................


# return the nth element of Fibonacci sequence
def fibonacci(n):
    """Our recursion ends when the number reduces to 1.
    This is called the base condition.
    Every recursive function must have a base condition
    that stops the recursion or else the function calls itself infinitely.
    The Python interpreter limits the depths of recursion to help avoid
    infinite recursions, resulting in stack overflows.
    By default, the maximum depth of recursion is 1000. If the limit
    is crossed, it results in RecursionError."""
    if ( n < 2 ):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
