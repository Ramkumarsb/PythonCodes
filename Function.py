'''
# # Function:
# Where actual logic resides
# Default Function
def my_name():
    print("My Name is Ramkumar...")
    print("I am learning Python")


my_name()

def greet():
    print("Hi there")
    print("Well come")


greet()

# input in function or Positional argument function
def greeting(name, l_name):
    print('\n',f"Hello {name}{l_name}")
    print("How are you?")



greeting('sabastin','David')

def greet(name):
    print(f"hi {name}")


greet('Ram.s')
print(greet('Ram.s'))  # by default function return None.

def get_greeting(name):
    return f"Hi {name}"


print(get_greeting("Basvakumar"))

def incriment(no1,no2):
    return no1+no2
store = incriment(5,no2=2)
print(store)


# default parameter

def multiplication(x,y,z = 23):
    return x*y*z


print(multiplication(2,2))

def multiplication(x,y,z = 23,a): # lead to an error
    return x*y*z*a


print(multiplication(2,2))

# SyntaxError: parameter without a default follows parameter with a default


# passing Multiple arguments in single function
# we use asterisk followed by variable name i.e *Variable_name

def multiple_args(*variable_name):
    print(variable_name)


multiple_args('ramkumar',24,'time',2325,)



# key_value,args in function is achived by using **Variable_Name

print()
def dict(**args):
    print(args)
    print(args['Name'])


dict(Name = 'Ram',l_Name ='Bannalle',USN = '3GN17ME062',Branch = 'Royal Mech')



print('\n')

#Fizz_buzz
def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "Fizz_Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num


print(fizz_buzz(10))

def none_fun(helo):
    key = 'Lock'


none_fun(120)

# def grt(name):
#     mesg = 'a'
#     print (name)
# # print(grt('ss'))
# grt('KGF')

'''
# A recursive function is often defined as "a function that calls itself."

'''

def rfunc(n):
    print(n)
    if n>0:
        rfunc(n-1)


rfunc(4)

print()
def rfunc(n):
    if n==1:
        return 1
    else:
        return n + rfunc(n-1)


print(rfunc(100))


# Factorial of numbers

def fact(n):
    if n== 0:
        return 1
    else:
        return n*fact(n-1)


print(fact(5))


def my_name():
    print("My Name is Ramkumar...") ; print("I am learning Python")



my_name()

def local_variables():
    v1 = "My Name is Ramkumar..."
    v2 = "I am learning Python"
    print(v1,v2)
    print(v1,"\n",v2)
    print(v1+v2)


local_variables()

def function_name():
    a = 10
    b = 20
    c = a+b
    d = b-a
    e = a * b
    f = b/a
    print("a:", a, "b:",b,"c=a+b:",c,"d=b-c:",d,"e=a*b:",e,"f=b/a:",f)


# function_name()

def rfunc(n):
    if n>0:
        print(n)
        rfunc(n-1)


rfunc(5)
print("**************************")
def nfunc(j):
    print(j)
    if j>0:
        nfunc(j-1)


nfunc(5)

'''

# lambda function:
square = lambda x:x**2
num =[1,2,3,4,5]
m1 = map(square,num)
squares = list(map(square,num))
print(m1)
print(squares)