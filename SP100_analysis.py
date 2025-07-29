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


