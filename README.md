# Election Analysis
## Project Overview
For this project, a Colorado Board of Elections employee has requested a simple election audit from a recent local election. The audit requests included:
- A calculation of the total number of votes cast
- A complete list of the candidates
- The total number of votes received by each candidate
- Calculate the percentage of votes won by each candidate
- Determine the winner of the election
- The total number of votes cast in each county
- Calculate the percentage of votes cast by voters in each county
- Determine the county with the highest voter turnout

## Resources
- Data Source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.9.12, Visual Source Code 1.68.1

## Summary
The analysis of this election produced the following results:
- Total number of votes cast: 369, 711
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidates results were as follows:
  - Charles Casper Stockham:  23.05% of the vote with a total number of 85,213 votes
  - Diana DeGette:  73.81% of the vote with a total number of 272,892 votes
  - Raymon Anthony Doane:  3.14% of the vote with a total number of 11,606 votes
- **The winner of the election was Diana Degette.**

- The counties included in this election were:
  - Jefferson
  - Denver
  - Arapahoe
- The voter turnout by county was:
  - Jefferson: 10.5% of voters (a total of 38,855 voters) in this election were from Jefferson County
  - Denver: 82.8% of voters (a total of 306,055 voters) in this election were from Denver County
  - Arapahoe: 6.7% (a total of 24,801 voters) in this election were from Arapahoe County
- **The county with the largest voter turnout in this election was Denver County**

## Analysis
The entire script for this analysis can be found [here](PyPoll_Challenge.py).

One of the more complicated portions of written code for this analysis included the following script to differentiate between candidates (or counties) and then count the number of votes for each key within that variable:
```
# If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
```

## Future Usage
One of the major benefits of the way this particular script was written is its ability to be utilized in different elections and with different variables being considered. This script was written with almost no references to specific cells or ranges within the data, allowing it to be easily manipulated to function in *any* election and assess a large number of potential variables.

Some potential suggestions for modifying this script to make it even more adaptable for future use include:
##### The script should be rewritten to choose which variable to measure based off of user input.
This would allow for the exact same script to run through any number of variables with which the user might be interested. This allows the script to become fully adaptable, regardless of the formatting of the csv.

For example, if the following code were added before reading the csv file

```
# Ask what variable to measure
column_number = int(input("In which column (counting from left to right) is the information that you want to analyze located? (Numeric answers only, please)"))
```

This would prompt the user to input which column they are attempting to analyze. Once they provide the script with their answer, we could simply modify the script to read:

```
candidate_name = row[(column_number)-1]
```

as opposed to:

```
candidate_name = row[2]
```

It is important to note the user input must be converted into an integer in order for this to work, due to the mathematical calculation required in the second string of code. By including this user input feature, the script becomes far more adaptable and capable of running for any number of variables.

##### The script should be simplified to run a single loop, but allow for endless user inputs.
The script is currently written in such a way that both variables being measured are coded separately in one longer string of code. By adding a user-input feature into this script, it can be simplified to run the same loop endlessly on different variables until the user is satisfied.

This can be accomplished by adding the following code:

```
# Create a continuous loop:
while True:

    # Ask what variable to measure
    column_number = int(input("In what number column number (counting from left to right) is the information that you want to analyze located?"))
    
    #Create a condition in which the loop will end:
    if column_number =="":
        break
```

This would allow the script to be endlessly useful to the user: with just a few quick inputs, any user (not just those who understand Python) would be able to quickly identify the highest turnout for innumerable variables, ie: which county had the largest voter turnout, which candidate had the largest percentage of votes, which state had the highest turnout, which party, etc.

## Conclusion
By making a few minor adjustments, a simple analysis for a specific Board of Elections in Colorado is able to become useful for any election data anywhere. This particular script was able to answer some questions for our clients in Colorado, but may end up being beneficial for even more clients in the future.
