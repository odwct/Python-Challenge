import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Path to collect my data
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Set to store unique values
total_votes = 0
candidates = []

# Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
#A complete list of candidates who received votes
    Charles_Casper_count = Diana_count = Raymon_Anthony_count = 0
    Charles_Casper_percent = Diana_percent = Raymon_Anthony_percent = 0

 # Read through each row of data after the header
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate == "Charles Casper Stockham":
            Charles_Casper_count += 1
        elif candidate == "Diana DeGette":
            Diana_count += 1
        elif candidate == "Raymon Anthony Doane":
            Raymon_Anthony_count += 1

#The total number of votes each candidate won
Results = {"Charles":Charles_Casper_count, "Diana DeGette":Diana_count, "Raymon":Raymon_Anthony_count}

#The percentage of votes each candidate won
Charles_Casper_percent = round((Charles_Casper_count / total_votes) * 100, 3)
Diana_percent = round((Diana_count / total_votes) * 100, 3)
Raymon_Anthony_percent = round((Raymon_Anthony_count / total_votes) * 100, 3)

#The winner of the election based on popular vote
Winner = max(Results, key=Results.get)

# Formating results to print
Prt_Analysis = f"""
Election Results 
--------------------------------------
Total Votes: {total_votes}
--------------------------------------
Charles Casper Stockham:{Charles_Casper_percent}% ({Charles_Casper_count})
Diana DeGette:{Diana_percent}% ({Diana_count})
Raymon Anthony Doane: {Raymon_Anthony_percent}% ({Raymon_Anthony_count})
--------------------------------------
Winner: {Winner}
--------------------------------------"""

print(Prt_Analysis)

# Open a new text file with the results
with open("PyPoll.txt", "w") as file:
    file.write(Prt_Analysis)
    file.close()
