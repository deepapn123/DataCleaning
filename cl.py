#Categorical Data Cleaning
import pandas as pd
import numpy as np

def isnumeric_ornull(value):
    try:
        if(float(value) or value==""):
            return True
    except (ValueError, TypeError):
        return False
    
# Create a simple DataFrame

df = pd.read_csv('ms.csv')

print("\n Original Data Frame: \n")
print(df)

# checking for invalid data for column 'NAME' and then removing it 


for value,x in zip(df['NAME'],df.index):
    if isnumeric_ornull(value):
        df=df.drop(x)
print("\n\n After cleaning NAME field\n")       
print(df)
    
    
           
     


