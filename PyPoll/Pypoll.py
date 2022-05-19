pypoll_csv = 'PyPoll/Resources/election_data.csv'

total_votes = 0
stockham_counter = 0
degette_counter = 0
doane_counter = 0

with open("PyPoll/Resources/election_data.csv", 'r') as f:
    f.readline()
    #create "for each" loop
    for line in f:
        #find total vote count
        total_votes = total_votes + 1 
        
        #split file into three parts, and count each candidate. I looked at the csv to see that there were only three candidates. 
        #If there were more, I would have needed to create a loop that spit out each unique name.
        parts = line.split(',')
        if parts[2] == "Charles Casper Stockham\n":
            stockham_counter = stockham_counter + 1
        elif parts[2] == "Diana DeGette\n":
            degette_counter = degette_counter + 1
        elif parts[2] == "Raymon Anthony Doane\n":
            doane_counter = doane_counter + 1
max_votes = max(stockham_counter, degette_counter, doane_counter)
winner = ""
if max_votes == stockham_counter:
    winner = "Charles Casper Stockham"
elif max_votes == degette_counter:
    winner = "Diana DeGette"
elif max_votes == doane_counter:
    winner = "Raymon Anthony Doane"

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Charles Casper Stockham: " + str(round(stockham_counter / total_votes * 100, 3)) + "% (" + str(stockham_counter) + ")")
print("Diana DeGette: " + str(round(degette_counter / total_votes * 100, 3)) + "% (" + str(degette_counter) + ")")  
print("Raymon Anthony Doane: " + str(round(doane_counter / total_votes * 100, 3)) + "% (" + str(doane_counter) + ")")   
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")


with open("PyPoll/analysis/pypoll_analysis.txt", "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write("Total Votes: " + str(total_votes)+ "\n")
    f.write("-------------------------\n")
    f.write("Charles Casper Stockham: " + str(round(stockham_counter / total_votes * 100, 3)) + "% (" + str(stockham_counter) + ")\n")
    f.write("Diana DeGette: " + str(round(degette_counter / total_votes * 100, 3)) + "% (" + str(degette_counter) + ")\n")  
    f.write("Raymon Anthony Doane: " + str(round(doane_counter / total_votes * 100, 3)) + "% (" + str(doane_counter) + ")\n")   
    f.write("-------------------------\n")
    f.write("Winner: " + winner + "\n")
    f.write("-------------------------\n")