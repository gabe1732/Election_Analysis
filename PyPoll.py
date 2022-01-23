# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path. this imports the file that contains the data you need. "file_to_load" is the new name that you will use to reference throughout the code.  This is easier then referencing the origianl file.  Makes easier to copy code
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.  this creates the file and the location of the final output.  This is easier then referencing the origianl file.  Makes easier to copy code 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter. This line is used when you are trying to tally counts or amounts up when going through the loop.  Here we would like to count the votes so we set votes to zero and then below as it goes through each line it will add 1 for each loop to the vote counter
total_votes = 0

# Candidate options; this is the place holder to create a list of unique values in a column we chose below.  In the exampe we are looking for the candidates names so every time a new name is found in the file it is added to this list. [] creates a list
candidate_options = []

# 1. Declare the empty dictionary.  A dictionary is linking to items together like writing agent code to writing agent or policy number to writing agent.  this exampe we are linking one vote to a specific candidate. {} creates the link
candidate_votes = {}

# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.  the "with open" will open the file that you are importing above. "file_to_load" and all of the data in that file is not considered "election data" so now when we want to look at the data we reference election_data.  
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    # Read the file object with the reader funtion.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    
    # this is the beginning of the loop for each row in the file_reader or election_data we are going to count it as one vote
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        
        # print the candidate name from each row.  for every row in the loop we are going to add the names in row 2 (0,1,2) column 3 zero counts as a row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate... we nee to add and if statement.  If we do not add a if statement it will just add the name from every line we only want the unique names.  
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list. this adds the candidates name to the candidate option above
            candidate_options.append(candidate_name)
            
            #2. Begin tracking that cadidates's votes count. this is creating the connection between candidate votes and candidate name we assigned candidate name in as row 2 above and setting it to zero
            candidate_votes[candidate_name] = 0 
            
            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
# Save the results to our tect file.
with open(file_to_save, 'w') as txt_file:
    
#Print the final vote count to the terminal.
    election_results = (f"\nElection Results\n"
                        f'----------------------------\n'
                        f'Total Vots: {total_votes:,}\n'
                        f'--------------------------\n')
    print(election_results, end="")
        # Save the final vote count to the text file. 
    txt_file.write(election_results)
    
    # Determin the percentage of votes for each candidate by looping through the counts
    # 1. Look through the candidate list.  
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: Print out each cadidate's name, cote count and percentage of votes to the terminal
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        
        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote counte and Candidate
        # Deteremine if the votes is greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            # and, set the winning_cadidate equal to the cadidate's name. 
            
    winning_candidate_summary = (f'---------------------------\n'f'Winner: {winning_candidate}\n'f'Winning Vote count: {winning_count:,}\n'f'Winning Percentage: {winning_percentage: .1f}%\n'f'----------------------------\n')
    print(winning_candidate_summary)
    # Save the winning candiate's results to the text file.
    txt_file.write(winning_candidate_summary)   
    
    
    

# To do: print out the winning cadidate, vote count and percentate to terminal

    
    # 4. Print the cadidate name and percentage of votes.
    #print(f'{candidate_name}: received {vote_percentage}% of the vote.')
 
     
    
#     # To do: perform analysis.
#     print(election_data)

# #using the with statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:
    
#     # Write some data to the file.
#     txt_file.write("Counties in the election\n--------------------------\nArapahoe\nDenver\nJefferson")




# The we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 






 