import pandas as pd

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

print(df)
print()
# Find everyone that lives in Riverside
print(df.loc[df['City'] == 'Riverside'])
print()
# Find everyone that lives in Riverside and has a first name of John
print(df.loc[(df['City'] == 'Riverside') & (df['First'] == 'John')])


df['Tax %'] = df['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25) 
# print(df)
df['Taxes Owed'] = df['Income'] * df['Tax %']
print(df)
print()
to_drop = ['Area Code', 'First', 'Address']
df.drop(columns=to_drop, inplace=True)
print(df)

df['Test Col'] = False
print(df)
print()
df.loc[df['Income'] < 60000, 'Test Col'] = True
print()
print(df)
# Group BY
print()
print(df.groupby(['Test Col']).mean().sort_values('Income'))