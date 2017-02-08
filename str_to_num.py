def str_to_num(string_num):
    """ Convert a string to a positive integer
        >>> print str_to_num("123")
        123

        >>> print str_to_num("-123")
        -1

        >>> print str_to_num("abc")
        -1
    """

    val = 0
    i = 0

    if not string_num.isdigit():
        return -1

    for char in reversed(string_num):
        val += (ord(char) - 48) * (10 ** i)
        i += 1

    return val 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print    


 
 
     