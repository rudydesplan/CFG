import pandas as pd
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Task 1. Read the data from the spreadsheet

read = pd.read_csv(r"C:\Users\rudy\Documents\GitHub\CFG\Python Programming\Project 3\sales.csv")
#print(read)

#Task 2. Collect all of the sales from each month into a single list

sales_month = read.groupby(["month"])["sales"].sum()
#print(sales_month)

#Task 3. Output the total sales across all months

total_sales = read["sales"].sum()
#print(f"The total sales across all months is : {total_sales}")

#Extension 1. Output the total sales across all months

spreadsheet = pd.pivot_table(read, index=["month"])
new_spreadsheet = spreadsheet.drop(['year'], axis = 1)
#print(new_spreadsheet)

#Extension 2b. Calculate the average

annual_mean = sales_month.mean(axis = 0)
#print(f"The average sales across the year is : {annual_mean}")

#Extension 2c. Calculate the months with the highest and lowest sales

sales_sorted = read.sort_values("sales", axis = 0, ascending = False)

highest_sales = sales_sorted["sales"].head(n=1).to_list()
#print(f"The highest sales across the year is : {highest_sales[0]}")

lowest_sales = sales_sorted["sales"].tail(n=1).to_list()
#print(f"The lowest sales across the year is : {lowest_sales[0]}")

# Use a data source from a different spreadsheet
# For this part we use a kaggle dataset about car_sales in the U.S

sales = pd.read_csv(r"C:\Users\rudy\Documents\GitHub\CFG\Python Programming\Project 3\Car_sales.csv")
Porsche = sales.loc[sales['Manufacturer'] == 'Porsche'] # extracted the lines with the Porsche value
Analyzed_data = Porsche.drop(['Manufacturer'], axis=1)
#print(Analyzed_data)

# started preparing the visualization of various indicators
sns.lineplot(x="Engine_size", y="Price_in_thousands", data=Analyzed_data)
#plt.title('Engine_size Vs Price_in_thousands')
#plt.show()

sns.lineplot(x='Horsepower', y='Price_in_thousands', data=Analyzed_data)
#plt.title('Horsepower Vs Price_in_thousands')
#plt.show()

sns.lineplot(x='Price_in_thousands', y="Sales_in_thousands", data=Analyzed_data)
#plt.title("Sales_in_thousands Vs Price_in_thousands")
#plt.show()