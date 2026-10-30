"""This module counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

import os
import sys
from pathlib import Path
from collections import Counter
from time import strftime


COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}


def sort_by_value(item):
    """Create a key to be used to sort wordlist later."""
    return item[-1]


class WordProcess:
    """Processes a text file for word-count analysis."""

    def __init__(self):
        """Construct class instance and load the wordlist."""

        self.wordlist = {}
        self.words_in_manuscript = ""
        self.manuscript_file = ""
        self.word_count = {}
        self.results_list = []
    
        # Open and read the wordlist from the directory the script is in.
        wordlist_filename = "wordsEn.txt"
        wordlist_path = Path(sys.path[0]) / wordlist_filename
        
        print("  TO-DO: Open and read the wordlist from", wordlist_path)
        self.wordlist = {"one", "two", "three", "four"}
 

    def read_input_file(self, input_file_name):
        """
        Read the specified input file.
        Return True if file can be read; False if it cannot.
        """
        
        # Open and read the input file.
        self.manuscript_file = input_file_name
        
        print("  TO-DO: Open and read the manuscript from",
              self.manuscript_file)
        self.words_in_manuscript = ["one", "two", "three", "four",
                                    "TWO", "Three", "four", "THREE",
                                    "Four","four"]

        return True

    def analyze(self, suppress_common_words):
        """
        Compare input text file to English wordlist.
        Count word frequencies and obtain most common words.
        """
        print("  Compiling results, one moment ... ", end="")

        # Generate word counts of all words in the manuscript.
        count = 0

        for word in self.words_in_manuscript:
            # Strips lowercase words and punctuation.
            word = word.lower().strip(".,?!\"\';:()")
            self.words_in_manuscript[count] = word
            count += 1

        self.word_count = dict(Counter(self.words_in_manuscript))

        print(f"read {count} words from manuscript file.")

        # Uses reverse order to sort (most frequent first).
        items = sorted(self.word_count.items(), key=sort_by_value,
                       reverse=True)

        # Get counts of 50 words that
        # appear most frequently in manuscript.
        self.results_list = []
        for word in items[:50]:
            # Suppress common words if requested by user.
            if suppress_common_words and word[0] in COMMON_WORDS:
                continue
            result = word[0] + ": " + str(word[1]) + " times"
            self.results_list.append(result)

    def print_list(self):
        """Print analysis results to screen."""
        print(f"\nResults for {self.manuscript_file}")
        for line in self.results_list:
            print("  " + line)

    def save_list(self):
        """Save analysis results to log files."""
        # Get path to current user's desktop.
        desktop_dir = Path("~/Desktop").expanduser()
        output_dir = Path(desktop_dir) / "WordCount_output"

        # Set output dir to be current working directory.
        print("  TO-DO: Set output folder to be", output_dir)

        # Save results to log file and copy to archive file.
        print("  TO-DO: Save results to log file and copy to archive file.")
 
        # List files currently in output dir.
        print("  TO-DO: List files currently in", output_dir)

        return True
