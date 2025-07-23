import pandas as pd

#creating a series
s = pd.Series([10,20,30,40])

print("series:\n", s)

#data frame
data = {
    'name' : ['alice', 'bob', 'charlie'],
    'age' : [25,30,35],
    'salary' : [2000, 3000, 4000]
}
df = pd.DataFrame(data)
print("data frame", df)

#printing top and last five rows
print("top five rows:\n", df.head())
print("top bottom five rows:\n", df.tail())
print(df.info)

#selecting column and rows
print( "column by name:\n", df['name'])
print("column by name:\n", df[['name','age']])
print("row by label:\n", df.loc(0))
print("print row by index\n", df.iloc(0))


#filtering and conditioning selection
print("older than 30:\n", df[df['age']>30])
print("filter by name:\n", df[df['name']=='alice'])

#data cleaning
print("all the null values:\n", df.isnull())
print("drop all the missing values:\n", df.dropna())
print("fill all the missing values with 0", df.fillna(0))

#renaming columns
df.rename(columns ={'age': 'years'}, inplace = True)
print("renamed column:\n", df.head())

#data aggregation
print("group by salary:\n", df.groupby('name')['salary'].sum())

#mean salary
print("mean of salary", df['salary'].mean())

#sorting and indexing
print("sorting age from a to z:\n", df.sort_values('years'))
df.set_index('name', inplace = True)
print("indexed data", df)


















