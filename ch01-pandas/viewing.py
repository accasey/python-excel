import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)

df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Number']

# print(df[['State', 'Area Code']])
# If there is a large amount of data, you can slice it. e.g. just look at the first three lines
# print(df['First'][0:3])
# You can view rows
# print(df.iloc[1])
# and a cell
# print(df.iloc[2,1])
# # or
# print(df.iloc[[2,1],[2,0]])

wanted_values = df[['First', 'Last', 'State']]
stored = wanted_values.to_excel('State_Location.xlsx', index=None)