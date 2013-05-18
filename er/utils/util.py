def ngrams(field, n):
    """ngrams returns all unique, contiguous sequences of n characters
    of a given field.
        
    :param field: the string to be 
    :param n: the number of characters to be included in each gram
    
    usage:
    >>> from dedupe.dedupe.predicated import ngrams
    >>> ngrams("deduplicate", 3)
    ('ded', 'edu', 'dup', 'upl', 'pli', 'lic', 'ica', 'cat', 'ate')
    """
    return tuple([field[pos:pos + n] for pos in xrange(len(field) - n + 1)])

def initials(field, n=None):
    """predicate which returns first a tuple containing
    the first n chars of a field if and only if the
    field contains at least n characters, or an empty
    tuple otherwise.
    
    :param field: the string 
    :type n: int, default None
    
    usage:
    >>> initials("dedupe", 7)
    ()
    >>> initials("deduplication", 7)
    ('dedupli', )
    >>> initials("noslice")
    ('noslice', )
    """
    return (field[:n], ) if n is not None or len(field) > n-1 else () 
