def q10_find_anagrams(word, word_list):
    """
    Finds all anagrams of 'word' from the 'word_list' and returns them.
    
    An anagram is a word formed by rearranging the letters of another word.
    
    Args:
        word (str): The reference word to find anagrams for
        word_list (list): A list of words to search
        
    Returns:
        list: A list of anagrams found in word_list
        
    Example:
        >>> q10_find_anagrams("listen", ["silent", "enlist", "hello", "world"])
        ['silent', 'enlist']
    """
    char_dict={} #empty dictionary for recording letters and their frequency of 'word'
    anagram_words_list= []
    #Records all the letters and their frequency and adds them to the dictionary
    for c in word:
        if c in char_dict:
            char_dict[c] += 1 
        else:
            char_dict[c] = 1
    
    for words in word_list:
        word_dict={} #empty dictionary for recording letters and their frequency of words in the word_list
        for char in words:
            if char in word_dict:
                word_dict[char] += 1 
            else:
                word_dict[char] = 1
        if char_dict == word_dict: #if the letters and their frequency match, we have anagrams
            anagram_words_list.append(words)
    return anagram_words_list
        

print(q10_find_anagrams("listen", ["silent", "enlist", "hello", "world"]))

