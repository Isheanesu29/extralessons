

import pandas as pd
import numpy as np

df = pd.read_csv('dir_pandas/2019 - Copy.csv',na_values=False)

add_columns = df['Overall rank'].map(str) + ' ' + df['Score'].map(str)
# add_columnss = df['Overall rank'].astype(float) + ' ' + df['Score'].astype(float)

df['Rank_Score'] = add_columns
df.rename(columns={'Score':'General'},inplace=True)

drop_column = df.drop(columns=['General'],inplace=True)

print()