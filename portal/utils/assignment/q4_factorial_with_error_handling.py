def q4_safe_factorial(n):
    """
    Returns the factorial of n.
    
    - Returns None if n is negative or not an integer.
    
    Args:
        n: The input number
        
    Returns:
        int or None: The factorial of n, or None if n is invalid
        
    Example:
        >>> q4_safe_factorial(5)
        120
        
        >>> q4_safe_factorial(-5)
        None
    """
    #checks if 0 or negative
    if n <= 0:
        return None 
    #Tabulation method is used for calculation of factorial.
    dp = [0] * (n+1) #creates a list of 0s of length n+1

    dp[0] = 1 # 0! = 1
    dp[1] = 1 # 1! = 1

    for i in range(2, n+1): #iterates from 2 to n(inclusive)
        dp[i] = i * dp[i-1] #changes the value of list from 0 to the factorial of the number.
    return dp[-1] #returns the last number of the list
#limitation: 
#This approach might be time efficient but it consumes more space since all of the 
#factorials are stored in the list.
print(q4_safe_factorial(-5))
