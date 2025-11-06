import pandas as pd
import re

def isnumeric_ornull(value):
    try:
        if(float(value) or value==""):
            return True
    except (ValueError, TypeError):
        return False
    
# Create a simple DataFrame

df = pd.read_csv('ms.csv')

print(df)

# checking for invalid data for column 'NAME' and then removing it 


for value,x in zip(df['NAME'],df.index):
    if isnumeric_ornull(value):
        df=df.drop(x)
    special_chars = re.findall(r'[^a-zA-z0-9\s.]',value)
    if special_chars:
        df=df.drop(x)
print("\n After Cleaning: \n")       
print(df)
    
    
           
     

