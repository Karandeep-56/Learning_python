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


# Calculate % change from previous day — gives daily returns
returns = df.pct_change()
print("\n Daily returns\n", returns)


# Let's say our portfolio has:
# - 0% in AAPL
# - 50% in AMZN
# - 25% in TSLA

weights = np.array([0, 0.50 , 0.25])

#calculate mean daily return of each stock
mean_daily_return = returns.mean()

#portfolio return is average weighted returns of individual return
port_return = np.sum(mean_daily_return* weights )

print("\n portfolio return (Daily average)", port_return)


#Cumulative Return (Compound over time)
portfolio_returns = returns.copy(deep=  True)
portfolio_returns['Portfolio']= portfolio_returns.dot(weights)

#compounding the returns over time gives cumulative return
cumulative_return = (1+ portfolio_returns).cumprod()

#plotting cumulative return
cumulative_return["Portfolio"].plot(title = "portfolio cumulative return")
plt.xlabel("date")
plt.ylabel("cumulative Return")
plt.grid(True)
plt.show()





