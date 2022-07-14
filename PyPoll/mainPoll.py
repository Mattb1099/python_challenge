import os
import csv

from sqlalchemy import false


electionData_csv = os.path.join( "PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("PyPoll", "Analysis", "poll_analysis.txt")

#Open and read csv
with open(electionData_csv, newline = '') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read the header row first
    csv_header = next(csv_file)

    #Read through each row after the head
    Total_votes = 0
    Charles_votes = 0
    Diana_votes = 0
    Raymon_votes = 0
    for row in csv_reader:
        Total_votes = Total_votes + 1
        if row[2] == 'Charles Casper Stockham':
            #counts the number of rows that
            Charles_votes =  Charles_votes + 1
        if row[2] == 'Diana DeGette':
            #counts Diana votes
            Diana_votes = Diana_votes + 1
        if row[2] == 'Raymon Anthony Doane':
            #counts Raymon votes
            Raymon_votes = Raymon_votes + 1

    Charles_percent = Charles_votes / Total_votes * 100
    Diana_percent = Diana_votes / Total_votes * 100
    Raymon_percent = Raymon_votes / Total_votes * 100
    Winner = false
    if Charles_votes > Diana_votes and Charles_votes > Raymon_votes:
        
        Winner = 'Charles Casper Stockham'
        
    elif Diana_votes > Charles_votes and Diana_votes > Raymon_votes:
        
        Winner = 'Diana DeGette'
        
    else:
        
        Winner = 'Raymon Anthony Doane'
    
   

     #Generates the output
    output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {Total_votes}\n"
    f"----------------------------\n"
    f"Charles Casper Stockham: {round(Charles_percent, 3)}({Charles_votes}) \n"
    f"Diana DeGette: {round(Diana_percent, 3)}({Diana_votes}) \n"
    f"Raymon Anthony Doane: {round(Raymon_percent, 3)}({Raymon_votes}) \n"
    f"----------------------------\n"
    f"Winner: {Winner}\n")
   

  #Print the output (to terminal)
    print(output)
# Export the results to text file
    with open(file_to_output, "w") as txt_file:
     txt_file.write(output)



