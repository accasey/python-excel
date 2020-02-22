import pandas as pd
import numpy as np

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

df.drop(columns='Address', inplace=True)

df = df.set_index('Area Code')
print(df.loc[8074])
print(df.iloc[0])

print(df.loc[8074:, 'First'])
print(df.First.str.split(expand=True))

df.First = df.First.str.split(expand=True)
# print(df)

# Both of these methods work
# df.replace(np.nan, '-', regex=True, inplace=True)
df = df.replace(np.nan, '-', regex=True)

#
to_excel = df.to_excel('modified.xlsx', index=None)
