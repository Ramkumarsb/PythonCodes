# Code to built calculator.
print("Enter 1 for ADD, 2 for subtraction, 3 for multiplication and 4 for division...")
operation = int(input("Enter inbetween 1 to 4? "))
if operation == 1:
    num1 = int (input("Enter number:"))
    num2 = int(input("Enter another number"))
    sum = num1+num2
    print("Sum of two number is "+ str(sum))
elif operation == 2:
    num1 = int(input("Enter number:"))
    num2 = int(input("Enter another number"))
    sub = num1 - num2
    print("Subtraction of two number is "+str(sub))
elif operation == 3:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter another number"))
    mul = num1 * num2
    print("Multiplication of two number is " + str(mul))
elif operation == 4:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter another number "))
    div = num1 / num2
    print("Division of two number is" + str(div))
else:
    print("< invalid input>")
