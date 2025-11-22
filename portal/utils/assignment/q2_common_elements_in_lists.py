def q2_common_elements_in_lists(list1, list2):
    """
    Takes two lists and returns a set of elements that appear in both lists.
    
    - Works for any data type (numbers, strings).
    - Handles empty lists gracefully.
    
    Args:
        list1 (list): The first list
        list2 (list): The second list
        
    Returns:
        set: A set of elements that appear in both lists
        
    Example:
        >>> q2_common_elements_in_lists([1, 2, 3, 4], [3, 4, 5, 6])
        {3, 4}
    """
    # Converts the lists into sets for semantic fit
    set1 = set(list1)
    set2 = set(list2)
    common_set = set()

    #Iterates through the members of first set and checks if the member is in second set
    for x in set1:
        if x in set2:
            common_set.add(x)
    return common_set

print(q2_common_elements_in_lists([1, 2, 3, 4], [3, 4, 5, 6]))
            
