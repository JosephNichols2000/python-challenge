#importing dependancies
import os
import csv
from datetime import datetime

#printing top line/title
print('Financial Analysis')

#setting path to variable
pybankpath = os.path.join('PyBank','Resources','budget_data.csv')

#create a list to store dictionaries 
data_list = []

#reading in the csv file using DictReader
with open(pybankpath, 'r') as csvfile:
    pybankcsv = csv.DictReader(csvfile)
   
    for row in pybankcsv:
        data_list.append(row)

#making a copy of the original data list
data_list_copy = data_list

#finding the total numer of months included in the dataset
total_months = len(data_list)
print(f'Total Months: {total_months}')

#variable for storing net profit/losses
total_sum_of_profit = 0

#finding and printing the net total amount of profit/losses over the entire period
for row in data_list:
    profit_loss = int(row['Profit/Losses'])
    total_sum_of_profit += profit_loss
print(f'Total: ${total_sum_of_profit}')

#converting date column to datetime format for correct sorting
date_format = '%b-%d'

for row in data_list:
    date_string = row['Date']
    new_date_format = datetime.strptime(date_string, date_format)
    row['Date'] = new_date_format

#finding the changes in profit/losses across the period and storing them to a list
changes = []
for i in range(1, len(data_list)):
    date_change1 = int(data_list[i]['Profit/Losses']) 
    date_change2 = int(data_list[i-1]['Profit/Losses'])        
    date_changes = date_change1 - date_change2       
    changes.append(date_changes)

#sum and then average of the profit/losses
average_change = sum(changes) / len(changes)
print(f'Average Change: {average_change}')

index_max = changes.index(max(changes))
index_min = changes.index(min(changes))
max_date = data_list[index_max+1]['Date']
min_date = data_list[index_min+1]['Date']

#finding the largest and smallest amounts in changes
print(f'Greatest Increase in Profits: {datetime.strftime(max_date, "%b-%d")} {max(changes)}')
print(f'Greatest Decrease in Profits: {datetime.strftime(min_date, "%b-%d")} {min(changes)}')

#text file with data results
results_txt = 'pybank_results.txt'
with open(results_txt, 'w') as file:
    file.write('Financial Analysis\
    Total Months: 86\
    Total: $22564198\
    Average Change: -8311.105882352942\
    Greatest Increase in Profits: Aug-16 1862002\
    Greatest Decrease in Profits: Feb-14 -1825558')