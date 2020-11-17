#usr/bin/env python
import sys
import argparse

##if len(sys.argv) != 2:
##    print("Usage: ")
##    sys.exit()
##a = sys.argv[1]
##b = sys.aegv[2]
parser = argparse.ArgumentParser(description="A program to illustrate command line\
argument parsing")
parser.add_argument('numbers', type = int, nargs ='+', help="a set of numbers")
parser.add_argument('--add','-a',action ='store_true', default = False, help = 'sum the numbers')
args = parser.parse_args()
print(dir(args))
print(args.numbers)

sum = a + b
print("The sum is: ", sum)
print(args.add)

if args.add is True:
    result = sum(args.numbers)
print("The result is", result)
