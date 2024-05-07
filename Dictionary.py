
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

alternative_dic = {
    "Sun" : "Moon",
    "Earth" : "Sky",
    "Land" : "Water",
    "Light" : "White"
}
print(alternative_dic)

# -------------------------------------
# Nested DIC

D = dict(
    emp1 ={'Name':"Bob","Job":"Mang"},
    emp2 ={'Name':"Kim","job":"Dev"},
    emp3 ={'Name': "Sam",'Job':"Dev"}
)
print(D)

D = dict(
    e1={'Name':"Bob","Job":"Mang"},
    e2={'Name':"Kim","job":"Dev"},
    e3={'Name': "Sam",'Job':"Dev"}
)
print(D)

print("ZIP of Dict")

Ids = ['Emp1','Emp2','Emp3']
EmpInf = [
    {'Name':"Bob","Job":"Mang"},
    {"Name":"Kim","Job":"Dev"},
    {"Name":"Sam","job":"Dev"}
]

mearg = dict(zip(Ids,EmpInf))
print(mearg)


Ids = ['Emp1','Emp2','Emp3']
EmpInf =  {'Name':'',"Job":''}
defaultValue = dict.formkey(Ids,EmpInf)


"""
Ids = ['Emp1','Emp2','Emp3']
EmpInf =  {'Name':"","Job":""}
print( dict.fromkeys(Ids,EmpInf))
print(dict(zip(Ids,EmpInf)))
"""



person = {
    "Name":"John Paul",
    "age":30,
    "city": "NYC"
}
print(person)

# Accessing perticular elemint:

print(person["Name"])
person["age"] = 45
print(person)

# adding a new key value pair:
print("adding a new key value pair:")
person["Profession"] = "Software Engineering"
print(person)

# removing a new key value pair:
print("# removing a new key value pair:")
del person["age"]
print(person)
