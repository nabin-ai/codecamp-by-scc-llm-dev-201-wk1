def q9_sum_numbers_in_text(text):
    """
    Takes a string and sums all the numbers found in the text using regex.
    
    Args:
        text (str): The input text
        
    Returns:
        int: The sum of all numbers found in the text
        
    Example:
        >>> q9_sum_numbers_in_text("I have 3 apples and 4 oranges")
        7
    """
    t = list(text) #Breaks the paragraph into a list of characters
    sum = 0
    for char in t:
        if char.isdigit(): #checks if the char is a digit
            sum+= int(char) #adds the digit
    return sum

print(q9_sum_numbers_in_text("I have 3 apples and 4 oranges"))
