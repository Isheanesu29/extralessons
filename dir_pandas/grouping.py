

import pandas as pd

df = pd.read_csv('dir_pandas/2019 - Copy.csv',na_values=False)

getGDP_median = df['GDP per capita'].median()
getGDP_mean = df['GDP per capita'].mean()
print(f'the meadian is {getGDP_median}')
print(f'the mean is {getGDP_mean}')

describe = df.describe()
get_count = df['Christians'].value_counts()
get_countPercentage = df['Christians'].value_counts(normalize=True)
get_countByYes = df['Christians'].value_counts().loc['Yes']

get_groupby = df.groupby('Christians')
get_groups = get_groupby.get_group('Yes')
print(get_groupby)

num =  [2, 4, 6, 8, 10, 11.5, 12.7 ]
dnum = pd.DataFrame(num)
print(dnum.mean())
print(dnum.median())
