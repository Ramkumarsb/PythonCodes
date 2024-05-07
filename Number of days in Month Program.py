 # program greeting
print('This program will dsplay nmber of days in a given month')
 # init
valid_input = True
# get user input
month = int(input('Enter the month(e.g 1-12): '))
# determine num of days in month

# february
if month == 2:
     year = int(input('Enter the year(e.g 2010): '))
     if (year % 4 == 0) and not((year % 100 == 0) or (year % 400 == 0)):
         num_days = 29
     else:
         num_days = 28
         # january, march, may, july, august, october, december
elif month in (1, 3, 5, 7, 8, 10, 12):
     num_days = 31
# april, june, september, november
elif month in (4, 6, 9, 11):
     num_days = 30
# invalid input
else:
     print(valid_input)
     print('* Invalid Value Enterd -',month,'*')
     valid_input = False
if valid_input:
     print(valid_input)
     print('There are', num_days,'days in the month')