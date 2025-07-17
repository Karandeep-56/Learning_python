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
print("data frame", pd.DataFrame(data))