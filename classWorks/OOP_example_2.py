#!usr/bin/env python3

class Employee:
    def __init__(self,name,idnum,salary=0):
        self.name = name
        self.idnum = idnum
        self.salary = salary
    def work(self):
        print(self.name, "does stuff")
    def giveraise (self,percent):
        self.salary = self.salary + (self.salary * percent/100)
    def __mul__(self,num):
        return (self.salary*num)
    def __add__(self,other):
        return (self.salary + other.salary)
    def __str__(self):
        return "Employee: %s, ID: %d, Salary: %.2f" %(self.name,self.idnum,self.salary)

class Chef(Employee):
    def __init__(self,name,idnum):
        Employee.__init__(self,name,idnum,salary=500000)
    def work(self):
        print(self.name, "makes food")
class Manager(Employee):
    def __init__(self,name,idnum):
        Employee.__init__(self,name,idnum,salary=75000)

    def giveraise(self,percent, bonus = 0.1):
        Employee.giveraise(self, percent + bonus)
if __name__ == "__main__":
    e = Employee ("Sam", 11111, salary = 30000)
    e2 = Employee ("Jennifer", 11121, salary = 30800)
    print(e.name, e.salary, e.idnum)
    print(e*2)
    print(e+e2)
    print(e)

    print()
    c1 = Chef("Bill", 11113)
    c1.work()
    print(c1)
