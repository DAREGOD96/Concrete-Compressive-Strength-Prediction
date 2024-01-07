import sys


def error_message_details(error, error_details: sys):
    """
    Extracts details from the given error and error_details.

    Parameters:
    - error: Exception
        The exception for which details need to be extracted.
    - error_details: module 'sys'
        The sys module containing information about the error.

    Returns:
    str
        A formatted error message including the Python script name, line number, and error message.
    """
    _, _, exc_tb = error_details.exc_info()
    error_message = "Error occurred in python script name[{0} line number [{1}] error message [{2}]]".format(
        exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(error)
    )

    return error_message

    
class CustomException(Exception):
    """
    Custom exception class that extends the base Exception class.

    Attributes:
    - error_message (str): The error message associated with the exception.
    - error_details: The details or context information related to the exception.

    Methods:
    - __init__(self, error_message, error_details):
        Initializes the CustomException object with the provided error message and details.

    - __str__(self):
        Returns a formatted error message when the object is printed.
    """

    def __init__(self, error_message, error_details):
        """
        Initializes the CustomException object.

        Parameters:
        - error_message (str): The error message associated with the exception.
        - error_details: The details or context information related to the exception.
        """
        # Call the parent class's __init__ method
        super().__init__(error_message)

        # Assign the error message and details to instance variables
        self.error_message = error_message
        self.error_details = error_details

    def __str__(self):
        """
        Returns a formatted error message when the object is printed.

        Returns:
        str: Formatted error message.
        """
        return self.error_message

    
    