# This program will display the unicode for "Hello world!"
print("The unicode ending for 'Hello world!' is...")
print()
print(ord('H'),ord('e'),ord('l'),ord('l'),ord('o'),\
ord('w'),ord('o'),ord('r'),ord('l'),ord('d'),ord('!'))

#Age in seconds
import datetime
birth_date = datetime.date(1998,5,15)
end_date = datetime.date.today()
age_days = (end_date-birth_date).days
age_sec = age_days*24*60*60
print('Age in days:',age_days)
print('age in seconds:',age_sec)
  