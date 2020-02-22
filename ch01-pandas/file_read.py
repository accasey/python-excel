import pandas as pd
# from openpyxl.workbook import Workbook

# Normally needs a path, but in the current working directory
df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_txt = pd.read_csv('data.txt', delimiter='\t')

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']
# print(df_excel)
# print(df_csv)
# print(df_txt)

df_csv.to_excel('modified.xlsx')