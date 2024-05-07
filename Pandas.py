'''
import pandas as pd
phone_book = {
    'Jhon':['857297000','john@xyzmail.com'],
    'Bob':['799488000', 'bob@xyzmail.com'],
    'Tom':['9749552647','tom@xyzmail.com']
}
series = pd.Series(phone_book)
print(series)



import pandas as pd
import numpy as np
# simple arry
data = np.array(['R','A','M','K','U','M','A','R'])
ser = pd.Series(data)
print(ser)


# empty Data frame
import pandas as PD
df = PD.DataFrame()
print(df)



# from list of lists
import pandas as pd
data = [
    ['Tom',10],['John',15],['Nick',14]
]
df = pd.DataFrame(data,columns=["Name","Age"])
print(df)

data1= [
    ['Hi',1524,'kick'],
    ['Jai',5697,'Mike']
]
df = pd.DataFrame(data1,columns=["String1","No.","Str2"])
print(df)



# From a Dictionary of ndarrays/Lists

import pandas as f
data_dict = {
    'Name':['tom','Nick','Jail'],
    'Age':[10,15,14]
}
df = f.DataFrame(data_dict)
print(df)


# Using Pandas Lib Fun for csv

import  pandas as pd
df = pd.read_csv('data.csv',sep=',',header='infer',
                 index_col=None)
print(df)


# Adding Column to existing DataFrame
import pandas as pd
data_dict2 = {
    'E_Name':['Ravi','Roshan','Vinod','Sailu'],
    'E_Id':[123,234,145,125],
    'E_Qualification':['MSC','BA','MBA','MCA']
}
df = pd.DataFrame(data_dict2)
E_Address = ['Hyderabad','Delhi','Lucknow','Vijaywada']
df['Address'] = E_Address
print(df)
# retriving single column
print(df['E_Name'])
print(df.E_Qualification)
'''

import pandas as pd
cat_data =pd.read_csv('Bike_Sales_2021.csv',index_col=0)
print(cat_data)
