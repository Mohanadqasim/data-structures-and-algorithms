import string
def repeated_word(input_string):
    # Step 1: Convert to lowercase and remove punctuation marks
    translator = str.maketrans('', '', string.punctuation)
    input_string = input_string.lower().translate(translator)
    
    # Step 2: Split into individual words
    words = input_string.split()
    
    # Step 3: Initialize set to track encountered words
    encountered = set()
    
    # Step 4: Find first repeated word
    for word in words:
        if word in encountered:
            return word
        else:
            encountered.add(word)
    
    # Step 5: No repeated words found
    return None