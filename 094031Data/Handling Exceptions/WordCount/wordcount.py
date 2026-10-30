"""This module initializes the WordCount program,
which counts the words in a manuscript."""

from validate import input_yesno
from wordprocess import WordProcess


# Create new instance of WordProcess class to perform the analysis.
word_process = WordProcess()
print("Welcome to the F&A text-analysis program.\n")

# Continue to prompt until user provides a file that can be read.
while True:
    input_file = input("What file do you want to analyze? ")
    successful_read = word_process.read_input_file(input_file)
    if successful_read:
        break

# Analyze manuscript, passing in user's choice to suppress common words.
ok_to_suppress_common = input_yesno("Strip common words from the results?")
word_process.analyze(ok_to_suppress_common)

# Print results of the analysis.
word_process.print_list()

# Save a log of results, if user chooses.
ok_to_save = input_yesno("Would you like to output these results to a file?")
if ok_to_save:
    word_process.save_list()
