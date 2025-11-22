"""W1D3 Q9 - Extract Dates

Extract dates in DD/MM/YYYY format.

Example:
    >>> q9_extract_dates("Event on 25/12/2024 and 01/01/2025")
    ['25/12/2024', '01/01/2025']
"""

import re


def q9_extract_dates(text):
    """
    Extract dates in DD/MM/YYYY format.
    
    Args:
        text (str): The input string to search for dates
        
    Returns:
        list: A list of all dates in DD/MM/YYYY format
        
    Example:
        >>> q9_extract_dates("Event on 25/12/2024 and 01/01/2025")
        ['25/12/2024', '01/01/2025']
    """
    dates = re.findall(r'[0-9]+/[0-9]+/[0-9]+', text)
    # dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
    return dates
print(q9_extract_dates("Event on 25/12/2024 and 01/01/2025"))
