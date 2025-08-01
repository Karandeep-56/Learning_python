#Foodr analysis with pandas and numpy
from itertools import groupby

import pandas as pd
import numpy_practices as np
import psycopg2
from sqlalchemy import create_engine

#connecting to postgres with my credentials

db_user = "postgres"

db_pass = "admin"

db_host = "localhost"

db_port = "5432"

db_name = "Foodr"

engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

print("✅ Connected to the database successfully!")

#load tables into pandas dataframes

meals_df = pd.read_sql("SELECT * FROM MEALS", engine)
orders_df = pd.read_sql("SELECT * FROM ORDERS", engine)
stock_df = pd.read_sql("SELECT * FROM STOCK", engine)

print("sample meal data:\n", meals_df.head())
print("sample orders dara:\n", orders_df.head())
print("sample stock data:\n", stock_df.head())

#counting total unique meals and entries exists
print("unique number of meals", meals_df["meal_id"].nunique())
print("unique eateries:\n", meals_df['eatery'].nunique())


#Total revenue per meal
orders_df['order_revenue'] = (orders_df['order_quantity']*
         orders_df['meal_id'].map(meals_df.set_index('meal_id')['meal_price']))

revenue_per_meal = orders_df.groupby('meal_id')['order_revenue'].sum().reset_index()

revenue_per_meal = revenue_per_meal.merge(meals_df[['meal_id', "eatery"]], on = 'meal_id', how = "left")

print("revenue_per_meal", revenue_per_meal)

#top five revenue generating meals
print("top five meals", revenue_per_meal.sort_values (by = 'order_revenue',
ascending = False).head())

#proft per meal
meals_df['profit margin'] = meals_df['meal_price']- meals_df['meal_cost']

orders_df['meal_cost'] = orders_df['meal_id'].map(meals_df.set_index('meal_id')['meal_cost'])


orders_df['meal_price'] = orders_df['meal_id'].map(meals_df.set_index('meal_id')['meal_price'])

orders_df['total_cost']= orders_df['order_quantity']* orders_df['meal_cost']

orders_df['total_price'] = orders_df['order_quantity']* orders_df['meal_price']

orders_df['profit'] = orders_df['total_price'] - orders_df['total_cost']

profit_by_eatery = orders_df.merge(meals_df[['meal_id', 'eatery']], on = 'meal_id', how = 'left')  \
\
.groupby("eatery")["profit"].sum().sort_values(ascending=False).reset_index()

print("profit per eatery",profit_by_eatery)

#Analyze stock levels vs order
stocked = stock_df.groupby('meal_id')['stocked_quantity'].sum()
ordered = orders_df.groupby('meal_id')['order_quantity'].sum()

stock_vs_orders = pd.DataFrame({
    'stocked' : stocked,
     'ordered' : ordered
}).fillna(0)

stock_vs_orders['leftover'] = stock_vs_orders['stocked']- stock_vs_orders['ordered']

print( 'stock where leftover is negative:\n', (stock_vs_orders[stock_vs_orders['leftover']<0]))

#daily revenue
daily_revenue = orders_df.groupby('order_date')['total_price'].sum().reset_index()

daily_revenue["7 day avg"] = daily_revenue['total_price'].rolling(window = 7).mean()
print(daily_revenue.tail(10))





