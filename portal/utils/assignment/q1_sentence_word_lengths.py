import string
def q1_sentence_word_lengths(sentence):
    """
    Takes a sentence and returns a dictionary mapping each word to its length.
    
    - Ignores punctuation.
    - Treats words case-insensitively.
    
    Args:
        sentence (str): The input sentence to analyze
        
    Returns:
        dict: A dictionary where keys are words (lowercase) and values are their lengths
        
    Example:
        >>> q1_sentence_word_lengths("Hello, World!")
        {'hello': 5, 'world': 5}
    """
    cleaned_string = "" #Stores the words after removing all punctuations.
    word_len = {} #dictionary that stores the length of each word.
    s = sentence.casefold() #converts all the letters in the sentence to lower case
    #checks if punctuation, if not adds to the cleaned string
    for char in s:
        if char not in string.punctuation: 
            cleaned_string += char 
    words = cleaned_string.split()
    #maps the cleaned word with its length
    for word in words:
        word_len[word] = len(word)
    return word_len

print(q1_sentence_word_lengths("!nabin nab!n"))