def str_to_num(string_num):
    """ Convert a string to a positive integer
        >>> print str_to_num("123")
        123

        # >>> print str_to_num("-123")
        # TypeError:String to be converted is invalid

        # >>> print str_to_num("abc")
        # TypeError:String to be converted is invalid
    """

    val = 0
    
    if string_num is None or string_num == "":
        raise TypeError("String to be converted is empty or Null")

    if not string_num.isdigit():
        raise TypeError("String to be converted is invalid")

    # for char in reversed(string_num):
    #     val += (ord(char) - ord('0')) * (10 ** i)
    #     i += 1

    # Alternatively

    for char in string_num:
        val = val * 10 + (ord(char) - ord("0"))

    return val 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print    


 
 
     