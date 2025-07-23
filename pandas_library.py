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







