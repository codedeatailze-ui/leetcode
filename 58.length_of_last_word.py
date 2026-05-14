def last_word(s1):
    count = 0
    found_word = False
    
    for w in range(len(s1)-1, -1, -1):
        if s1[w] != " ":
            count += 1
            found_word = True
        elif found_word:
            return count
    
    return count