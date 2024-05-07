# Function Decorator:
'''
#     Functions  which take other functions as input, add additional functionalities to
#     it and return it is called Function Decorator.

# as we know function is a callable object, hence even decorator function is also
called and it returns modified function/Class.

Note: You cannot Modify the existing function.
'''
def modification(modify):
    def onemore():
        modify()
        # adding my reply
        print("Ram: ")
        print("Take 20m straight then right turn walk for 6m you will reach. ")

    return onemore
'''
Let me reply with address.
'''
# Function decorator
def modify(printer):
    def another():
        printer()
        # adding Modification
        print("Unknown: ")
        print("        "
              "Could you let me know where this address comes?")
    return another

# A normal Function()
def printer():
    print("Ram: ")
    print("    Hi, I am Ramkumar.")
    print("    How may I help you?")


printer = modification(modify(printer))
printer()
'''
Now I want reply for my printer() function.
"Could you let me know where this address come?"


#  Another example

'''


# Now I want to add another number
def adding_3rd_num(add_of_2num):
    def function():
        sum_2_num = add_of_2num()
        m = 100
        return sum_2_num+m
    return function
@adding_3rd_num

# Initial Function
def add_of_2num():
    k = 63
    l = 10
    return l+k

# add_of_2num = adding_3rd_num(add_of_2num)
print(add_of_2num())