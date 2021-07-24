

import pandas as pd
from tabulate import tabulate

df = pd.read_csv('dir_pandas/2019 - Copy.csv',na_values=False)

hd = df.head(10)
tl = df.tail(10)
shape = df.shape
locate = df.loc[10:50:2] # when you put a third number like on the example it will increase by that number in our case by 2
get_column = df['Country or region']
get_listOfColumns = df.columns # this will print just the column's names
get_listOfColumnsWithData = df[['Overall rank', 'Country or region', 'Score']].head(15)
get_rowsAndColumns = df.loc[15:30,['Overall rank', 'Country or region', 'Score']]
filter_row = df.loc[df['Score'] > 7,'Score']
gh = df.Score > 7
filter_lamda = df.Score.loc[lambda x: x > 6]
get_location = df.iloc[:,2]
get_locationList = df.iloc[1:7,[2,3,5]]
filter_byQuery = df.query('Score < 7').iloc[:,2]
df = df.rename(columns= {'Country or region':'Country'})
# filter_Country = df.query('Country == ["Finland","Austria","Denmark","Norway"] & Score > 7,5')
countries = ["Finland","Austria","Denmark","Norway", "Gabon", "Switzerland","South Sudan"]
compare_countries = df['Country'].isin(countries)
get_countries = df.loc[compare_countries,'Country']
# languages = df['Languages'].str.contains('English')
languages = df['Languages'].str.upper()
get_languages = df.loc[languages,'Languages']

print()



