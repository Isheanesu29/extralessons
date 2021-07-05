

import pandas as pd
from tabulate import tabulate

df = pd.read_csv('dir_readWriteFiles\Sample.csv')
data = pd.DataFrame(df)

filt_column1 = data['Consignee_Name']=='TO THE ORDER OF BANK OF CEYLON' # this function will give you access to the specified column
filt_columns = data['Quantity'] < 50    # when you are trying to extract a data that contains a certain amount quantity use == or > or <
count = data.loc[filt_columns,'Quantity']
filt_row = data.loc[4]          # you use this code if you want to work with the row only 
count2 = data['Consignee_Name'].isin(filt_column1)
# comparison = data['Consignee_Name'].str().__contains__('BANK')
number_of_columns = data.columns
print(number_of_columns)

