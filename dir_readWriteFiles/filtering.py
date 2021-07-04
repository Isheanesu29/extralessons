

import pandas as pd
from tabulate import tabulate

df = pd.read_csv('dir_readWriteFiles\Sample.csv')
data = pd.DataFrame(df)

print(data)