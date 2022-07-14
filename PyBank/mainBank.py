
import os
import csv

from sympy import total_degree


budgetData_csv = os.path.join( "PyBank","Resources", "budget_data.csv")
file_to_output = os.path.join("PyBank", "Analysis", "budget_analysis.txt")

#Open and read csv
with open(budgetData_csv) as csv_file: 
    csvReader = csv.reader(csv_file, delimiter = ",")

    #Read the header row first
    csv_header = next(csv_file)

    #Read through each row after the head and sets variables
    months = 0
    total = 0
    month_of_change = []
    net_change_list = []
    greatest_increase = ["", -9999999999999999999]
    greatest_decrease = ["", 9999999999999999999]
    prev_net = 0
    for row in csvReader:
        #Counts number of months
        months = months + 1
        #counts the total
        total += int(row[1])
        #List of value changes
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]] 
        #Calculates the highest change in values
        if net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change
           #Calculates the lowest change in values
        if net_change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = net_change
         
    # Calculates the Average Net Change
    net_monthly_avg = ((sum(net_change_list) - net_change_list[0]) /( len(net_change_list) - 1 ))

    print(net_change_list)
    #print("Total months: " + str(months))
    #print("Total: " + str(total))
    #print("Average change: " + str(average))
    #print("Greatest increase in profits: ")
    #print("Greatest decrease in profits: ")
    #Generates the output
    output = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {months}\n"
   f"Total: ${total}\n"
   f"Average Change: ${net_monthly_avg:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

   # Print the output (to terminal)
print(output)
# Export the results to text file
with open(file_to_output, "w") as txt_file:
   txt_file.write(output)





