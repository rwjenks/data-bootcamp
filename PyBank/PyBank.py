# import dependencies
import os
import csv

# variables
total_months = 0
total_rev = []
net_profit = 0
greatest_inc = 0
greatest_dec = 0
greatest_inc_date = ""
greatest_dec_date = ""

# Module for reading CSV files
csvpath = os.path.join('..', 'budget_data.csv')
with open('budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    #skip header row
    csv_header = next(csvfile)

    # count months
    for row in csvreader:
        total_months = total_months + 1
        total_rev.append(float(row[1]))
        if int(row[1]) >= greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_date = row[0]
        if int(row[1]) <= greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_date = row[0]

# calculating average revenue change
# average_change = round(total_rev/total_months, 2)
net_profit = sum(total_rev)

# calculating average revenue change
average_change = round(sum(total_rev)/total_months, 2)

print("Financial Analysis")
print("--------------------------------------------")    
print("Total Months: " + str(total_months))
print(f"Total: {net_profit}")
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")")

#creating the new txt file
new_file = open("Output/analysis_1.txt", "w")

#writing the text file
new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write("Total Months: " + str(total_months) + "\n")
new_file.write("Total Revenue: $" + str(sum(total_rev)) + "\n")
new_file.write("Average Revenue Change: $" + str(average_change) + "\n")
new_file.write("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")" + "\n")
new_file.write("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")" + "\n")