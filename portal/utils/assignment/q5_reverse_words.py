import string

def q5_reverse_words(sentence):
    """
    Takes a sentence and returns a new sentence with each word reversed, 
    but the word order remains the same.
    
    - Ignores punctuation.
    
    Args:
        sentence (str): The input sentence
        
    Returns:
        str: A new sentence with each word reversed
        
    Example:
        >>> q5_reverse_words("Hello, World!")
        "olleH, dlroW!"
    """
    word_list = sentence.split() #Splits the sentences into words and stores them as list
    reversed_word_list = [] 
    for word in word_list:
        punct= ""
        reversed_core_word = ""
        for i in range(len(word)):
            #checks if punctuation. If yes, stores the character in punct.
            if word[i] in string.punctuation:
                punct = word[i] + punct
            else:
                reversed_core_word = word[i] + reversed_core_word #Starts adding the characters from behind to reverse it.
        reversed_word_list.append(reversed_core_word + punct)
    # print(reversed_word_list)
    return " ".join(reversed_word_list)

print(q5_reverse_words("Hello, World!"))