import pandas as pd
import path
import os
from datetime import datetime
import sys

csvpath = "raw_data/budget_data_1.csv"
budget = pd.read_csv(csvpath)
budget.head()

#Assigning Var to find total number of months in dataset
total_month = budget["Date"].count()
total_month

#Assigning Var to find total revenue in the dataset
total_revenue = budget["Revenue"].sum()
total_revenue

#Finding the average marginal monthly change in revenue
i = 0
marginal_rev = 0
while marginal_rev in budget["Revenue"]:
    marginal_rev = budget["Revenue"][i + 1] - budget["Revenue"][i]
    i += 1
avg_change = marginal_rev/total_month
avg_change

#Assign Var for minimum revenue and which month
min_rev = budget.min()
min_rev

#Assign Var for maximum revenue and which month
max_rev = budget.max()
max_rev

#printing findings from above to a text file
bank_findings = (
print("Financial Analysis for Spreadsheet 1")
print("------------------------------------")
print("Total Months: " + str(total_month))
print("Total Revenue: " + str(total_revenue))
print("Average Revenue Change: " + str(avg_change))
print("Greatest Increase in Revenue: " + str(max_rev))
print("Greatest Decrease in Revenue: " + str(min_rev))
)
sys.stdout = open(file, 'w')
print(bank_findings)
