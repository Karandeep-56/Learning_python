#portfoli analysis with detailed explanation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#sample price data for apple, tesla and Amazon for over 4 days
data = {
   'AAPL': [105.05, 106.25, 104.75, 107.35],
   'AMZN': [310, 315, 312, 320],
   'TSLA': [250, 252, 248, 255]
}
dates = pd.date_range('2022-01-01', periods = 4)
df = pd.DataFrame(data, index = dates)
