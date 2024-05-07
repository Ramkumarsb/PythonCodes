# Pre-Requisites to Understand Function Decorator
'''
> Function as Object.
we can pass a function as an argument into another function....
>> Nested Function / Inner Function
    >---->  if a function is inside another function then it is Nested function
    Why Inner Function ?
    1. Inner Function acts as helper for outer function
    2. It acts as a kind of encapsulation.
    3. Decorator/ Closure

">>> Function as Parameter "
        # We Can pass function as parameter into another function.

>> Aliasing Function

>>Returning function


'''

# Function as Object.

def add(a,b):
    return a+b

def sub(a,b):
    return b-a

def maths(fun,a,b):
    return fun(a,b)

print(maths(add,2,3))
print(maths(sub,2,3))


# Nested Function / Inner Function

def lib(cabin1,cabin2,cabin3):
    print("Inside the Library..")
    print(f"Well Come to Library. Your at {cabin1}")
    def book(b1,b2):
        print(f"I am reading {b1}.")
        print(f"By sitting in {cabin2}.")
        print("I suggest you to read "+ b2)

    book("The Leader Who had no Title","The Secret")

    return cabin3


print(lib("Resipsion","School","Library will closs at 9:30 pm."))

def outerfun(name,lastname):
    def innerfun():
        return f"hello I am {name} {lastname}"


    print(innerfun())


outerfun("Joy",'Morish')


# Function as Parameter
# We Can pass function as parameter into another function.

def i_have_some_func(par):
    print("Some things never change...  " + par())

def eelse():
      return "Nothing is permanent"



i_have_some_func(eelse)

# example 2

def bonus():
    bon_off = 2000
    return bon_off

def salary(l):
    my_sal = 27000
    total_sal = l()+my_sal
    print("My salary is ", total_sal)

salary(bonus)

# Aliasing Function

def select():
    print("I am select Function's statement")

alias = select

alias()

# Returning function

def rec_func():
    def trac():
        print("Hello world")

    trac()
rec_func()

# Returning function
def rec_func():
    return "Hi Returning function"

def func(f):
    # print(f())
    return f


func(rec_func)
a = func(rec_func)
print(a())
print(a)

# Function Decorator:

def modify_exist_func(func_as_para):
    def additional_modification():
        print("E = MC^2")
        func_as_para()
        print("Life Never stopes!")


    return additional_modification



def exist_func():
    print("Enjoy Every Moment")
    print("keep moving!")


any_variable = modify_exist_func(exist_func)
any_variable()

# another way of Decorator function:
print("\nanother way of Decorator function:")
def sub(ppp):
    def minus_():
        ppp()
        s = ppp() - 30
        return s

    return minus_()

@sub
def add():
    a = 10
    b = 30
    c = a+b
    return c


print(add)

# ------------------------------

def unknow(r):
    def update():
        r()
        print( '''Unkown: \n        Hii, Could you please let me know 'Where does this address come?' ''')



    return update()

@unknow
def ram():
    print("Hello..! \n     I am Ram, how may I help you?")

ram