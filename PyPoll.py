# The data we need to retrieve
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
# Establish candidate name counter
candidate_options = []
# Initialize empty vote counting dictionary
candidate_votes = {}
# Winning Candidate and Winning Votes tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #read the headers
    headers = next(file_reader)
    # 1. The total number of votes cast
    for row in file_reader:
        total_votes +=1
        # 2. A complete list of candidates who received votes
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # 3. The total number of votes each candidate won
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
# save the results to a txt file
with open(file_to_save, "w") as txt_file:
    election_results = (f"\nElection Results\n"
    f"--------------------\n"
    f"Total Votes: {total_votes: ,}\n"
    f"--------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    # 4. The percentage of votes each candidate won
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        # print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.\n")
        # print to txt file
        candidate_results = (f"{candidate_name}: {vote_percentage: .2f}% ({votes:,})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)
    # 5. The winner of the election
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (f"--------------------\n" 
    f"Winner: {winning_candidate}\n" 
    f"Winning Vote Count: {winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage: .2f}%\n" 
    f"--------------------")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


