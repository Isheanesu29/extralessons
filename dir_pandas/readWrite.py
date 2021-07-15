


import pandas as pd
import numpy as np

df = pd.read_csv('dir_pandas/2019 - Copy.csv',na_values=False)

filt = (df['Score'] > 5) 
df_score = df.loc[filt]
df_score.to_csv('dir_pandas/2019 - Modified.csv') # create a csv file
df_score.to_json('dir_pandas/2019 - Modified.json',orient='records',lines=True) # create a json file

skip_rows = pd.read_csv('dir_pandas/2019 - Copy.csv',skiprows=3)
skipN_rows = pd.read_csv('dir_pandas/2019 - Copy.csv',nrows=4)

def updateCountryOrRegion(Country):
    return Country.upper()

def updateCountry(Country):
    if Country == 'Denmark':
        return Country.replace('Denmark','Zimbabwe')

def stripCountry(Country):
    if Country==('Finland has good weather'):
        return ' '

def stripCountry2(Country): # stripCountry2 is a function and it takes on a parameter or argument.
    if '//' in Country:
        return Country.replace('//','')
    else:
        return Country

def convetListToString(list):
    return ''.join(list)

  
# df = df['Country or region'].apply(updateCountryOrRegion) # inorder to place it back to the same dataframe remember to equals it to
df['country'] = df['Country or region'].apply(stripCountry2)
df['newList'] = df['preprocessed_docs'].apply(convetListToString)

print()
