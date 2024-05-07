#Calculating the Drake Equation.
print("Wellcome to the SETI program")
print("This program will allow you to enter specific value related to")
print("the likelihood of fing intelligent life in our galaxy. All")
print("percentage should be entered as integer value, eg. 40 and not .40")
print()

#get user input
P = int(input('What percentage of stars do you think have planets?: '))
n = int(input('How many planets per star do you think can support life?: '))
f = int(input('What percentage do you think actually develop life?: '))
i = int(input('What percentage of those do you think have intelligent life?: '))
c = int(input('What percentage of those do yoy think can communicate with us?: '))
L = int(input('Number of years you think civilization last?: '))

#calculate result
num_detecteable_civilizations = 7 * (P/100) * n * (f/100) * (c/100) * L 

#display result
print()
print('Based on the values you entered...')
print('these are an estimated',round(num_detecteable_civilizations),'potentially num_detecteable_civilizations in our \
galaxy.')
