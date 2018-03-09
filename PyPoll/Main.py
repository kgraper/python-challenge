#import dependencies
import os
import path
import pandas as pd
from datetime import datetime
import sys

#setting up file path
csvpath = "raw_data/election_data_1.csv"
#reading file
election_results = pd.read_csv(csvpath)
#seeing what the data looks like
election_results.head()

#calculating total votes
total_votes = election_results["Voter ID"].count()
total_votes

#creating variable for number of times Vestal was voted for
cand_1_votes = election_results.loc[election_results["Candidate"] == "Vestal"]
cand_1_votes.head(20)

#Calculating total number of votes for Vestal
cand_1_sum = cand_1_votes.count()
cand_1_sum

#Finding percentage of the votes in favor of Vestal
cand_1_percent = (cand_1_sum/total_votes)*100
cand_1_percent
#Calculations completed for Vestal, Move on to next candidate

#Starting Same process but for Candidate Torres
cand_2_votes = election_results.loc[election_results["Candidate"] == "Torres"]
cand_2_votes.head()

#Sum of Torres Votes
cand_2_sum = cand_2_votes.count()
cand_2_sum

#Percent for Torres
cand_2_percent = (cand_2_sum / total_votes)*100
cand_2_percent

#Starting for Seth
cand_3_votes = election_results.loc[election_results["Candidate"] == "Seth"]
cand_3_votes.head()

#all Seth calcs. in one
cand_3_sum = cand_3_votes.count()
cand_3_percent = (cand_3_sum/total_votes)*100
print(cand_3_sum[2],cand_3_percent[2])

#Starting for Cordin
cand_4_votes = election_results.loc[election_results["Candidate"] == "Cordin"]
cand_4_votes.head()

#all Cordin calcs. in one
cand_4_sum = cand_4_votes.count()
cand_4_percent = (cand_4_sum/total_votes)*100
print(cand_4_sum[2], cand_4_percent[2])


#printing the findings to a text file
poll_findings = (
print("Election Results (Percent: Total Votes)"),
print("---------------------------------------"),
print("Total Votes: " + str(total_votes)),
print("---------------------------------------"),
print("Vestal: " + str(cand_1_percent[0]) + ": " + (str(cand_1_sum[0])) ),
print("Torres: " + str(cand_2_percent[0]) + ": " + (str(cand_2_sum[0]))),
print("Seth: " + str(cand_3_percent[0]) + ": " + (str(cand_3_sum[0]))),
print("Cordin: " + str(cand_4_percent[0]) + ": " + (str(cand_4_sum[0]))),
print("---------------------------------------"),
print("Winner: Vestal"),
print("---------------------------------------")
)
output_file = open(results_file.txt, 'w')
output_file.write("Election Results (Percent: Total Votes)"),
output_file.write("---------------------------------------"),
output_file.write("Total Votes: " + str(total_votes)),
output_file.write("---------------------------------------"),
output_file.write("Vestal: " + str(cand_1_percent[0]) + ": " + (str(cand_1_sum[0])) ),
output_file.write("Torres: " + str(cand_2_percent[0]) + ": " + (str(cand_2_sum[0]))),
output_file.write("Seth: " + str(cand_3_percent[0]) + ": " + (str(cand_3_sum[0]))),
output_file.write("Cordin: " + str(cand_4_percent[0]) + ": " + (str(cand_4_sum[0]))),
output_file.write("---------------------------------------"),
output_file.write("Winner: Vestal"),
output_file.write("---------------------------------------")

