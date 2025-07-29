#sp100 analysis using numpy

import numpy as np
import matplotlib.pyplot as plt
import csv

#load csv with structured datatypes (assuming no missing values )
data = np.genfromtxt('sp100.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')
print("all company names and sectors")

for company in data:
    print(f"{company['Name']} ({company['Sector']})")
