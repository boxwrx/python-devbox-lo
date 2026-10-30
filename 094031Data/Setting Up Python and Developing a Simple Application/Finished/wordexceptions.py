"""This module includes custom exception classes for the WordCount program."""


class FileEmptyError(Exception):
    """Creates an exception for use when a WordCount input file is empty."""
    pass


class FileTooBigError(Exception):
    """
    Creates an exception for use when a WordCount
    input file exceeds a specified file size.
    """

    def __init__(self, size):
        """Construct class instance with file-size attribute."""
        self.size = size

    def __float__(self):
        """Format file size as type float."""
        return self.size
