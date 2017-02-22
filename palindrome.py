
def has_palindrome_permutation(given_string):
    """ Write an efficient function that checks whether any permutation of an input string is a palindrome
        >>> print has_palindrome_permutation("civic")
        True

        >>> print has_palindrome_permutation("ivicc")
        True

        >>> print has_palindrome_permutation("civil")
        False

        >>> print has_palindrome_permutation("livci")
        False
    """

    unpaired_characters = set()

    for char in given_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)  

    return len(unpaired_characters) <= 1 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print    
