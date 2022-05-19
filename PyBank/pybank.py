net_gain = 0
avg_gain = 0
greatest_inc = [None, float('-inf')] # [Month, greatest increase]
greatest_dec = [None, float('inf')]
total_months = 0
net_change = 0

with open("PyBank/Resources/budget_data.csv", 'r') as f:
    f.readline() # read the header line
    prev_gain = None 
    for line in f:
        total_months = total_months + 1
        parts = line.split(',')
        gain = int(parts[1])
        # find total gain
        net_gain = net_gain + gain

        # Avg compute helper
        if prev_gain:
            net_change = net_change + (gain - prev_gain)
        prev_gain = gain

        # Greatest increase 
        if gain > greatest_inc[1]:
            greatest_inc[0] = parts[0]
            greatest_inc[1] = gain

        # Greatest decrease
        if gain < greatest_dec[1]:
            greatest_dec[0] = parts[0]
            greatest_dec[1] = gain
avg_gain = net_change / total_months

        

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_gain))
print("Average Change: $" + str(avg_gain))
print("Greatest Increase in Profits: " + str(greatest_inc[0]) + " ($" + str(greatest_inc[1]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_dec[0]) + " ($" + str(greatest_dec[1]) + ")")


with open("PyBank/analysis/pybank_analysis.txt", 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total: $" + str(net_gain) + "\n")
    f.write("Average Change: $" + str(avg_gain) + "\n")
    f.write("Greatest Increase in Profits: " + str(greatest_inc[0]) + " ($" + str(greatest_inc[1]) + ")\n")
    f.write("Greatest Decrease in Profits: " + str(greatest_dec[0]) + " ($" + str(greatest_dec[1]) + ")\n")
