

import pandas as pd
import numpy as np

df = pd.read_csv('dir_pandas/2019 - Copy.csv',na_values=False)

drop_rows = df.dropna()    # will drop rows with missing values
drop_withArg = df.dropna(axis='columns',how= 'any') # will drop columns with any missing values
df.fillna(0,inplace=True)
convert_Score = df['Score'].astype(str) # change a datatype to whatever datatype you want
dataType = df.dtypes
get_uniqueValues = df['GDP per capita'].unique()
df.replace('Finland','Finnish',inplace=False)



print(dataType)