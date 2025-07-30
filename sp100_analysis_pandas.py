import pandas as pd
import matplotlib as plt
import seaborn as sns

#load the file
df = pd.read_csv("sp100.csv")

#add a column of P/E
df["P/E"] = df["Price"]/df["EPS"]

#top 10 companies by P/E
print("top 10 companies by P/E")
print(df.sort_values("P/E", ascending = False).head(10))

#sector wise P/E summary (mean,median, std)
print("\n2. sector wise P/E summary")
print(df.groupby("Sector")["P/E"].agg(["mean", "median", "std", "count"]))

