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


def dec_to_bin(num):
    """ Decimal to binary conversion
        >>> print dec_to_bin(5)
        101

        >>> print dec_to_bin(2)
        10
    """

    count = 0
    out = ""

    if num == 0 or num == 1:
        return num

    while (num > 1):
        rem = num % 2
        num = num / 2
        out = str(rem * 10**count) + out
        count += 1
        
    out = str(num) + out    
    return out    



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print    


 
 
     