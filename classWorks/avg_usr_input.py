#!usr/bin/env python3
numbers = 0
avg = 0

while True:
    num = input("Please give me a number or write 'Done': ")

    try:
        x = float(num)
        avg += x
        numbers +=1

    except ValueError:
        if num == "Done":
            break
        else:
            print("Please enter a number: ")
            
            
try:
    avg = avg/numbers
except ZeroDivisionError:
    print("No numbers entered, please try again")
else:
    #Executes if try completes without an exception
    print("The average is {:.2f}".format(avg))
