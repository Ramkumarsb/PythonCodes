'''
# exampe for while loop
sum = 0
current = 1
n = int(input('Enter value: '))
while current <= n:
    sum = sum + current
    current = current + 1
    print(sum,current)

# Example
count = 1
while count<=5:
    print(count)
    count += 1
print('out of while loop')


# While loop with else
count = 5
while count >0 :
    print(count)
    count -=1
else:
    print('else block')
    print('out of loop')

count = 1
while count <= 5:
    print(count)
    count +=1
    if count == 3:
        break
else:                               # this else is part of line number 28
    print('else statemnet')
print('out of loop')                    # this print() id outer statement '''



total = 0
num = int(input('Enter number (0 to quit): '))
while num  != 0:
    total = total + num
    num = int(input('Enter number (0 to quit): '))
print('Total is',total)


