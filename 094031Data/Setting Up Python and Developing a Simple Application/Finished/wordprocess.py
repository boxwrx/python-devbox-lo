"""This module counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

import os
import sys
from pathlib import Path
from collections import Counter
from shutil import copyfile
from time import strftime
from wordexceptions import FileEmptyError, FileTooBigError


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
        wordlist_path = Path.cwd() / wordlist_filename

        try:
            with open(wordlist_path, "r") as f:
                self.wordlist = f.read().split()
        except FileNotFoundError:
            sys.exit("Cannot read the wordlist file at " +
                     str(wordlist_path) +
                     "\nCheck to see if the file is missing or corrupted.\n")


    def read_input_file(self, input_file_name):
        """
        Read the specified input file.
        Return True if file can be read; False if it cannot.
        """

        try:
            # Open and read the input file.
            self.manuscript_file = input_file_name
            file_size = os.path.getsize(input_file_name)
            if file_size > 1e7:
                raise FileTooBigError(file_size / 1e6)
            if file_size == 0:
                raise FileEmptyError()
            print(f"  Manuscript size is {file_size} bytes.")

            with open(input_file_name, "r") as f:
                print("  Reading file, one moment...")
                self.words_in_manuscript = f.read().split()
                print("  File read successfully.")

            return True

        except FileNotFoundError:
            print("  The input file does not exist.")
            return False

        except FileEmptyError:
            print("  The input file is empty. There is nothing to analyze.")
            return False

        except FileTooBigError as e:
            print(f"  The input is {float(e):.1f} megabytes. "
                  "The maximum file size is 10 megabytes.")
            return False

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
        timestamp = strftime("%Y-%m-%d_%H.%M.%S")
        results = output_dir / (Path(self.manuscript_file).stem +
                                "_results.txt")
        archive = output_dir / (Path(self.manuscript_file).stem +
                                "_results_backup_" + timestamp + ".txt")

        # Create output dir if it doesn't exist.
        try:
            if not output_dir.exists():
                output_dir.mkdir()

        except OSError:
            print("  Can't detect or create output directory at " +
                  str(output_dir) + "\nThe results can't be saved.")
            return False

        # Save the results to a log file.
        try:
            with open(results, "w") as f:
                f.write(f"Results for {self.manuscript_file}:\n\n")
                for line in self.results_list:
                    f.write(line + "\n")

            print("  Log file saved to " + str(results))

        except PermissionError:
            print("  Can't save results file due to a permission error.\n" +
                  "  File or containing directory may be locked:\n  " +
                  str(results))

        except OSError:
            print("  Can't save results file due to a system error.\n  " +
                  str(results))

        else:
            # Only executes if log file successfully saved.
            try:
                # Copy archive file.
                copyfile(results, archive)

            except OSError:
                print("  Can't create the archive file:\n  " +
                      str(archive))

            else:
                print("  Archive file saved to " + str(archive))
 
        # List files currently in output dir.
        print(f"\nThe {output_dir} output directory now contains:")
        dir_contents = list(output_dir.iterdir())
        for item in dir_contents:
            if item.is_file():
                print("  " + item.name)

        return True
