import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the file
df = pd.read_csv("sp100.csv")

#add a column of P/E
df["P/E"] = df["Price"]/df["EPS"]

#top 10 companies by P/E
print("\ntop 10 companies by P/E")
print(df.sort_values("P/E", ascending = False).head(10))

#sector wise P/E summary (mean,median, std)
print("\n2. sector wise P/E summary")
print(df.groupby("Sector")["P/E"].agg(["mean", "median", "std", "count"]))

#Number of companies per sector
# df["Sector"].value_counts().plot(kind="bar", title="Companies per Sector")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.show()

#sector Wise Average EPS and Price (side-by-side bars)
# print("\n3 Sector Wise Average EPS and Price")
# sector_stats = df.groupby("Sector")[["Price", "EPS"]].mean().sort_values("Price")
# sector_stats.plot(kind = "bar", figsize= (10,6), title = "Sector Wise Average EPS and Price")
# plt.xlabel("Average Value")
# plt.tight_layout()
# plt.show()

#highlight Outliers (P/E > Q3 + 1.5×IQR)
print("\n4 Highlight outliers based on P/E")
q1 = df["P/E"].quantile(0.25)
q3 = df["P/E"].quantile(.75)
iqr = q3-q1
upper_bound = q3 + 1.5* iqr
outliers = df[df["P/E"]> upper_bound]
print("outliers ", outliers[["Name","P/E"]])

#correlaion between price and EPS
print("\n5 correaltion between price and EPS")
correlation = df["Price"].corr(df["EPS"])
print(f"correlation between price and EPS: {correlation:.2f}")

# 7. Scatter Plot: EPS vs. Price Colored by Sector
# print("\n6 Scatter Plot: EPS vs. Price Colored by Sector ")
# plt.figure(figsize = (10,6))
# sns.scatterplot( data = df, x = "EPS", y = "Price", hue = "Sector", palette = "Set2", s = 100)
# plt.title("EPS vs Sector by Price")
# plt.grid(True)
# plt.tight_layout()
# plt.show()
















