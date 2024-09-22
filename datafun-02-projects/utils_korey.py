Process:
In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offers methods to calculate mean and standard deviation.
'''

###########################################
# Import Modules at the Top
###########################################

import statistics

###########################################
# Declare global variables
###########################################

# Boolean variable to indicate if the company is the best company ever
is_best_company_ever: bool = True

# Integer variable for the number of years in biness
years_in_biness: int = 5

* Float variable for the average koreys pretty good homework scores
koreys_average_scores: float = 4.0

# List of strings representing the softwares i'm kind of sort of good at
skills_semi_mastered: list = ["Salesforce", "Excel", "Power_bi"]

# List of floats representing my latest and greatest homework scores
Koreys_pretty_good_homework_scores: list = [8.0, 3.0, 2.0, 8.0, 4.0]

###########################################
# Calculate Basic Statistics
###########################################

# Calculate basic stats using built-in functions min(), max() and statistics module functions mean() and stdev().
min_score: float = min(koreys_pretty_good_homework_scores)
max_score: float = max(koreys_pretty_good_homework_scores)
mean_score: float = statistics mean (koreys_pretty_good_homework_scores)
stdev_score: float = statistics.stdev(koreys_pretty_good_homework_scores)

###########################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
###########################################

byline: str = f"""
---------------------------------------------------------
2K Sales LLC : Reasonably priced shoes by a reasonable seller
---------------------------------------------------------
Is Best Company Ever: (is_best_company_ever}
Years in Biness: (years_in_biness)
Skills Semi Mastered: (skills_semi_mastered)
Koreys Pretty Good Homework Scores: (koreys_pretty_good_homework_scores)
Minimum Pretty Good Homework Scores: {min_score}
Maximum Pretty Good Homework Scores:{max_score}
Mean Pretty Good Homework Scores: {mean_score:.2f}
Standard Deviation of Pretty Good Homework Scores:{stdev_score:.2f}
"""

###########################################
# Define the get_byline() Function
###########################################

def get_byline() -> str: 
    '''Return a byline for my analytics projects."'
    return byline

###########################################
# Define a main() function for this module.
###########################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
