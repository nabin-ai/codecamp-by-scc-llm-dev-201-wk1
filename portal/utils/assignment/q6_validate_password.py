def q6_validate_password(password):
    """
    Checks if a password string meets the following conditions:
    
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    
    Args:
        password (str): The password string to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Example:
        >>> q6_validate_password("ValidPass123")
        True
        
        >>> q6_validate_password("weakpass")
        False
    """
    count = 0 #counter for number of characters
    #Flags to track if all the character types are met
    digit= False 
    upper = False
    lower =False
    #Iterate through each character in the password
    for char in password:
        if char.isdigit(): #checks for at least 1 digit
            digit = True
        if char.isupper(): #checks for at least 1 uppercase character
            upper = True
        if char.islower: #checks for at least 1 lowercase character
            lower = True
        count+=1 #Increment character count
    if digit and upper and lower and count>=8: #checks if all criteria are met
        return True
    else:
        return False

print(q6_validate_password("Nabin13"))