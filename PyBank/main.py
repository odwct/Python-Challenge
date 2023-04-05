import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Path to collect my data
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Set to store unique values
months = []
profits = []


def average_change(profit_losses):
    changes = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]
    avg_change = sum(changes) / len(changes)
    return avg_change

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

#The total number of months included in the dataset
    for row in csv_reader:
        current_month = row[0] # Amount is in first column
        amount_str = row[1] # Amount is in second column
        months.append(current_month)  # Add to set of unique months
        current_profit = int(amount_str) # Convert amount to integer
        profits.append(current_profit)

# The greatest increase in profits (date and amount) 
differences = [profits[i+1] - profits[i] for i in range(len(profits)-1)]
max_increase = max(differences)
max_index = differences.index(max_increase)
max_month = months[max_index+1]

# The greatest decrease in profits (date and amount)
max_decrease = min(differences)
min_index = differences.index(max_decrease)
min_month = months[min_index+1]

#The total number of months included in the dataset
# Count number of unique months
num_months = len(months) 
#The net total amount of "Profit/Losses" over the entire period
# Sum all amounts
Total_Profit_Losses = sum(profits) 

#The changes in "Profit/Losses" over the entire period, 
avg_change = round(average_change(profits), 2)

Prt_PyBank_Analysis = f"""
Financial Analysis
---------------------------------------------
Total Months: {num_months}
Total Profit & Losses: ${Total_Profit_Losses}
Average Change: $ {avg_change}
Greatest increase in Profits: {max_month} (${max_increase})
Greatest decrease in Profits: {min_month} (${max_decrease})"""

print(Prt_PyBank_Analysis)

# Open a new text file with the results
with open("PyBank.txt", "w") as file:
    file.write(Prt_PyBank_Analysis)
    file.close()