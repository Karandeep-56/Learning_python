#sp100 analysis using numpy

import numpy as np
import matplotlib.pyplot as plt
import csv

#load csv with structured datatypes (assuming no missing values )
data = np.genfromtxt('sp100.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')
print("all company names and sectors")

for company in data:
    print(f"{company['Name']} ({company['Sector']})")

#compute and print average price and EPS
print("\naverage price and EPS")
avg_price =  np.mean(data['Price'])
avg_EPS =  np.mean(data['EPS'])
print(f'average price{avg_price:.2f} and EPS {avg_EPS:.2f}')



# 3. Compute P/E Ratio for each company and add it to a new array
print("P/E ratios")
pe_ratios = data['Price']/data['EPS']
print(pe_ratios)

#find the company with the highest P/E ratios
print("\n4 company with highest pe ratios")
max_index = np.argmax(pe_ratios)
print(f" {data['Name'][max_index]} {pe_ratios[max_index]:.2f}")



#filter and print all the companies where sector is financial
print("\n all the companies where sector is financial")
financial = data[data['Sector']== 'Financials']
for row in financial:
    print(f"{row["Name"]} {row['Price']}")

#count how many companies are in each sector
print("\n6 sector counts")
unique_sectors,counts =  np.unique(data['Sector'], return_counts = True)
for sector, count in zip(unique_sectors,counts):
    print(f"{sector}:{count}")

#sector Wise average
print(f"sector Wise average")
for sector in unique_sectors:
    mask = data['Sector']==sector
    sector_pe = pe_ratios[mask]
    print(f"{sector}: Average P/E {np.mean(sector_pe):.2f}")

#creating a histogram fro P/E ratios
# print("creating a histogram for P/E ratios")
# plt.hist(pe_ratios, bins = 10 , edgecolor = 'black')
# plt.title("distribution of P/E ratios")
# plt.xlabel("P/E ratios")
# plt.ylabel("frequency")
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# 9. Identify outlier P/E ratios (2 std above mean)
print("\n9. Outlier Companies")
mean_pe = np.mean(pe_ratios)
std_pe = np.std(pe_ratios)
outlier_mask = pe_ratios>(mean_pe + 2 * std_pe)
print("outliers")
print(f"{data["Name"][outlier_mask]}")


# 10. List top 5 companies with lowest P/E
print("\n10. Top 5 Companies with Lowest P/E")
sorted_indices = np.argsort(pe_ratios)
for idx in sorted_indices[:5]:
    print( f"{data['Name'][idx]}: {pe_ratios[idx]:.2f}")

    # 11. Export the original dataset with computed P/E as CSV
print("\n11. Exporting to sp100_with_pe.csv")
with open('sp100_with_pe.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Sector', 'Price', 'EPS', 'P/E'])
    for row, pe in zip(data, pe_ratios):
        writer.writerow([row['Name'], row['Sector'], row['Price'], row['EPS'], round(pe, 2)])



    # 12. Plot sector-wise average P/E as a bar chart
print("\n12. Sector-wise Average P/E Bar Chart")
sector_averages = [np.mean(pe_ratios[data['Sector'] == sec]) for sec in unique_sectors] 
plt.bar(unique_sectors, sector_averages)
plt.xticks(rotation = 90)
plt.ylabel("P/E ratios")
plt.title("sector wise average p/E")
plt.tight_layout()
plt.show()




