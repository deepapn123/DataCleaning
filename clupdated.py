#Catagorical data Cleaning NAME field
import pandas as pd
import re

def isnumeric_ornull(value):
    try:
        if(float(value) or value==""):
            return True
    except (ValueError, TypeError):
        return False
def issplchr(value):
      special_chars = re.findall(r'[^a-zA-z0-9\s.]',value)
      if special_chars:
          return True
     
dataset ={"NAME":['MEERA V L','123','NaN','#$AB','MILAN.V.M'],"GENDER":['F','M','M','F','M'],"AGE":[20,21,22,23,24]}
# Create a simple DataFrame

df = pd.DataFrame(dataset)

print(df)

# checking for invalid data for column 'NAME' and then removing it 


for value,x in zip(df['NAME'],df.index):
    if isnumeric_ornull(value):
        df=df.drop(x)
    if issplchr(value):
        df=df.drop(x)
print("\n After Cleaning: \n")       
print(df)
    
    
