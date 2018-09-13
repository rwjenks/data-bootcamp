# import dependencies
import os
import csv

total_votes = 0
candidates = {}
num_votes = []
vote_count = 0
candidates_percent = {}
winner = ""
winner_count = 0

# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'election_data.csv')
with open('election_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    #skip header row
    csv_header = next(csvfile)

     # count votes
    for row in csvreader:
        total_votes = total_votes + 1

        vote_count = vote_count + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
# percentages for each candidate
for key, value in candidates.items():
    candidates_percent[key] = round((value/vote_count) * 100, 2)

# finding the winner
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# creating new text file
new_file = open("Output/election.txt", "w")

# writing the new file
new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(total_votes) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")