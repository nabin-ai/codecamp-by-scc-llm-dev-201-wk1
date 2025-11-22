def q3_count_unique_characters(text):
    """
    Takes a string and returns the number of unique characters.
    
    - Ignores spaces and case.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        int: The number of unique characters (ignoring spaces and case)
        
    Example:
        >>> q3_count_unique_characters("Hello World")
        7
    """
    txt = text.replace(' ', '') #Eliminates Spaces
    t = txt.casefold() #converts into lower case for uniform checking 
    unique_char = set(t) #Set removes all the duplicates
    count = 0
    for char in unique_char:
        count += 1 #count each unique character
    return count

print(q3_count_unique_characters("Hello World"))
        
