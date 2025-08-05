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


# SECTION 5: RISK — VARIANCE AND VOLATILITY

# Risk in finance = Uncertainty in returns
# Variance: how far returns are from average (spread)
# Standard deviation = square root of variance = "volatility"

# Annualized Covariance matrix — how stocks move together
cov_matrix = returns.cov() * 250
print("\nAnnualized Covariance Matrix:\n", cov_matrix)
#Equal Weights (1/3 Each)
weights_eq = np.array([1/3, 1/3, 1/3])
returns = df.pct_change()
# Portfolio variance = W.T * CovMatrix * W
port_variance = np.dot(weights_eq.T, np.dot(cov_matrix, weights_eq))
port_stddev = np.sqrt(port_variance)

print("\nPortfolio Variance:", port_variance)
print("Portfolio Volatility (Std Dev):", port_stddev)

#annualized Return (Example)
# Assume AAPL was 105.05 → 99.75 over 38 months
apple_price = pd.Series([105.05, 99.75], index=pd.to_datetime(['2015-01-06', '2018-03-29']))
total_return = (apple_price.iloc[-1] - apple_price.iloc[0]) / apple_price.iloc[0]

months = 38
annualized_return = ((1 + total_return) ** (12 / months)) - 1
annualized_return_3y = ((1 + total_return) ** (1 / 3)) - 1
print("\nTotal Return:", total_return)
print("Annualized Return (Monthly base):", annualized_return)
print("Annualized Return (3 years):", annualized_return_3y)

#SHARPE RATIO- RISK ADJUSTED RATIO

# Sharpe Ratio = (Return - Risk-Free Rate) / Volatility
apple_return = apple_price.pct_change()
annualized_vol = apple_return.std() *np.sqrt(250)
risk_free_rate = 0.01 #assumed

sharpe_ratio = (annualized_return - risk_free_rate) / annualized_vol
print("\nSharpe Ratio (AAPL):", sharpe_ratio)

















