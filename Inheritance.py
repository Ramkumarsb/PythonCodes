# Inheritance...
'''
The process of aquering the properties of parent class by a subclass is called Inheritance.

Type of Inheritance...
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance

'''
# Single Iheritance....
#		A subclass will have a super class.

class Car():
    def Engine():
        print("Turbo Engine with 8000 cc..")
    def staring():
        print("Power staring")
    def break_sys():
        print("ABS System")
    def drive_type(self):   #instance method
        self.mes = "4 wheel drive.."
        print(self.mes)

Car.Engine()
c_obj = Car()
c_obj.drive_type()

print()
class Thar(Car):
    def door():
        print("2 door are present")

Thar.staring()
Thar.door()


# 2. Multiple Inheritance
#                       If a class is inherited by more than one class then it is called ....

# Parent class 1
class TeamMember(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


# Parent class 2
    class Worker(object):
        def __init__(self, pay, jobtitle):
            self.pay = pay
            self.jobtitle = jobtitle

    # Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker):
    def __init__(self, name, uid, pay, jobtitle, exp):
        self.exp = exp
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, pay, jobtitle)
        print("Name: {}, Pay: {}, Exp: {}".format(self.name, self.pay, self.exp))


TL = TeamLeader('Jake', 10001, 250000, 'Scrum Master', 5)


# Second example

class School():
    def morning_prayer(self):
        print("Before we begin we pray to god.")

    def periods(self):
        print("There are 8 class in a day")

    def break_time(self):
        self.br = "We have 2 breaks in whole day."
        print(self.br)
        self.br1 = "1 short break"
        print(self.br1)
        self.br3 = 'Lunch break'
        print(self.br3)

class Subject():
    def Total_Sub(self):
        print("There are 4 subject")

    def language(self):
        print("2 languages are part of studies")

class Teacher(School, Subject):
    def Physics(self):
        print("This is Physics class")


    def Maths(self):
        class_= 'Maths class'
        print(class_)

t_obj = Teacher()
t_obj.break_time()

print('\n')
t_obj.periods()
t_obj.Physics()

# Method Resolution Order (MRO)

class Tech_Gudget:
    def __init__(self):
        super().__init__()                                          # 3 2nd execution line
        print("Parent1 Constructor")


    def hardwear(self):
        print("They are physically present.")


    def softwear(self):
        print("Non Physical")


class Mechanical_Instr:
    def __init__(self):
        super().__init__()                                              # 4 execute 1st
        print('Class 2 Constructor')


    def divider(self):
        print("Divider is used to mark points, draw circle")


    def verniercalper(self):
        return "verniercalper measuring instrument "

class Engineering(Tech_Gudget,Mechanical_Instr):
    Name = "GNDEC"
    time = '2017-2021'

    def __init__(self):
        super().__init__()                                  # 2                     # calling Constructor
        print("Child class Constructor")

    def branch(self, BName):
        self.branch = BName
        print(self.branch)

obj = Engineering()                                        # 1

# 3. Multilevel Inheritance

'''
 In multi-level inheritance, the class inherits the feature of another derived class.

pp -----> qq -----> rr
'''

class Maths():
    def mm(self):
        print("Maths Class is going..")
    def add(self):
        a = 4
        b = 5
        print('add: ',a+b)


    def power(self,p,r):
        t = p**r
        print(t)


class Science(Maths):
    def _2nd_law(self,m,a):
        f = m*a
        print("force is ", f, 'N')


    def PE(self):
        print("Stored Energy is ....PE")


class Games(Science):
    def good(self):
        print("Well all student love Games period")

    def bad(self):
        print("Game class is fucked by Maths teacher...")

class Period(Games):
    def first(self):
        print("First period..")


obj = Period()
obj._2nd_law(6,9)
obj.mm()
obj.power(9,9)
obj.add()
obj.bad()


