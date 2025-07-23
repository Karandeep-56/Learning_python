#Foodr analysis with pandas and numpy
import pandas as pd
import numpy as np
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
print(revenue_per_meal.sort_values (by = 'order_revenue',
ascending = False).head())


