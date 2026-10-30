"""This module includes a function for performing input validation."""


def input_yesno(message):
    """
    Display an input prompt, showing specified message.
    Keep prompting until user enters y, n, yes, or no in any case text.
    Return response as True or False.
    """

    while True:
        user_input = input("\n" + message + " (Y/N) ").lower()
        if user_input in ["y", "yes", "n", "no"]:
            if user_input in ["y", "yes"]:
                return True
            else:
                return False
