import os
import csv

#File header
print("Election Results")
print("-----")

#csv file setting
csv_file = os.path.join('PyPoll','Resources','election_data.csv')

#list for csv data to be read into
e_data = []

#reading in csv and adding data to list 
with open(csv_file, 'r') as csvfile:
    pypollcsv = csv.reader(csvfile)
   
    for row in pypollcsv:
        e_data.append(row)

#finding total votes, -1 for headers
total_votes = len(e_data)-1
print(f'Total votes: {total_votes}')

#spacer line
print("-----")

#finding the candidates and adding them to a list
candidates = []

for i in range(1, total_votes+1):
   if e_data[i][2] not in candidates:
       candidates.append(e_data[i][2])

#finding votes per candidate
ccs = 'Charles Casper Stockham'
dd = 'Diana DeGette'
rad = 'Raymon Anthony Doane'
ccs_count = 0
dd_count = 0
rad_count = 0

for row in e_data:
    if row[2] == ccs:
        ccs_count += 1
    elif row[2] == dd:
        dd_count += 1
    elif row[2] == rad:
        rad_count +=1

#finding percentages for each candidate and formatting them
ccs_percent = ccs_count/total_votes 
dd_percent = dd_count/total_votes 
rad_percent = rad_count/total_votes 

formated_css_percent = format(ccs_percent, ".3%")
formated_dd_percent = format(dd_percent, ".3%")
formated_rad_percent = format(rad_percent, ".3%")

#printing final candidate results
print(f'{ccs}: {formated_css_percent} ({ccs_count})')
print(f'{dd}: {formated_dd_percent} ({dd_count})')
print(f'{rad}: {formated_rad_percent} ({rad_count})')

print("-----")

#storing candidate, candidate counts, determining winner by highest vote and printing winners name
final_scores = {"Chales Casper Stockham":ccs_count, "Diana Degette":dd_count, "Raymon Anthony Doane":rad_count}

winner = max(final_scores, key=final_scores.get)

print(f'Winner: {winner}')

#creating text file for results
election_results = "election_results.txt"
with open(election_results, "w") as file:
    file.write('Election Results\
-----\
Total votes: 369711\
-----\
Charles Casper Stockham: 23.049% (85213)\
Diana DeGette: 73.812% (272892)\
Raymon Anthony Doane: 3.139% (11606)\
-----\
Winner: Diana Degette')