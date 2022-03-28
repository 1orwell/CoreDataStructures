def count_unique(s):
    '''
    >>> count_unique("aabb")
    2
    '''
    # The bellow for loop is faster than with a list
    # using a list would have had O(n^2)
    # total O(n)
    seen_char = set() # O(1)
    for c in s: # O(n)
        if c not in seen_char: # O(1)
            seen_char.add(c) #O(1)
    #return seen_char #O(1)

    # iterate c through s, create set
    # return len({c for c in s}) # O(n)

    # convert word s to set, set has no repeats, take length
    return len(set(s)) # also O(n)