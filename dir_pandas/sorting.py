

import pandas as pd

df = pd.read_csv('dir_pandas/2019 - Copy.csv',na_values=False)

sort_byCountry = df.sort_values(by = 'Country or region')
sort_byCountryDescending = df.sort_values(by = 'Country or region',ascending=False)

sort_withIndex = df.sort_index()
sort_singleColumn = df['Country or region'].sort_values()
sort_byLargest = df['Score'].nlargest(10)
sort_bySmallest = df['Score'].nsmallest(8)

print()
