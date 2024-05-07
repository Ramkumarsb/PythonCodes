# Fundamental Concepts

# numeric literals

print(1240)
print(-1240)
print(.1240)
print(1,240)
print(0.1240)
print(1,024.46)
print(0o24)
print(0)

#Arthmetic overflow
print(1.5e200 * 2.0e210)
##Arthmetic underflow
print(1.0e-300 / 1.0e100)
print(1/3)
print(3*(1/3))

# Built in format function
print(12/5)
print(format(12/5,'.2f'))
print(5/7)
print(format(5/7,'.3f'))

#String literals
print('hello')
print("Jennifer, Smith's friend")

#print('''Let's go!''')



#Control characters

#New line
print("Hello\nworld")
#Horizontal tab
print("Hello\tworld")
#single Quote
print("Hello\'world\'")
#double Quote
print('Hello\"world\"')
#backslash
print("Hello\\world")



#String formating
print(format('Hello','<20'))
print(format('Hello','>20'))
print(format('Hello','^20'))
print(format('Hello world','.<30'),'Have a nice day!')
print(format('hello world','^40'))
print(format('-','-<20'),'Hello world',format('-','->20'))



# Line Joining
i = [1,2,3,4,
5,6,7,8]
print(i)
string = 'I am ram.\
 how are you?'
print(string)





