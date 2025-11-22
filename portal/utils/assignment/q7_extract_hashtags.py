import re

def q7_extract_hashtags(text):
    """
    Extracts all hashtags from a text string using regex.
    
    - Returns a list of hashtags without the # symbol.
    
    Args:
        text (str): The input text
        
    Returns:
        list: A list of hashtags without the # symbol
        
    Example:
        >>> q7_extract_hashtags("Check out #python and #coding!")
        ['python', 'coding']
    """

    #Regex to capture all the words that start with '#'
    #r"#+(\w+)" matches all the words that start with '#' and are followed by letters, digits and underscore. It ignores any other punctuations.
    hashtags = re.findall(r"#+(\w+)", text)
    
    return hashtags

print(q7_extract_hashtags("Check out #python! and ##coding!"))
