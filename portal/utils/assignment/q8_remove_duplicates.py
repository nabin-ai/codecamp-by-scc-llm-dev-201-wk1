def q8_remove_duplicates(items):
    """
    Takes a list and returns a new list with duplicates removed, 
    preserving the original order.
    
    Args:
        items (list): The input list
        
    Returns:
        list: A new list with duplicates removed, in original order
        
    Example:
        >>> q8_remove_duplicates([1, 2, 2, 3, 4, 3, 5])
        [1, 2, 3, 4, 5]
    """
    # items_set = set(items)
    num_list = []
    for num in items:
        if num in num_list: #If number already exists, then skip.
            continue
        else:
            num_list.append(num)
    return num_list
    # return list(items_set)
print(q8_remove_duplicates([1, 2, 2, 4, 3, 3, 5]))
