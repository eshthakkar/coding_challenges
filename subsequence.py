# Time complexity of both solutions is O(n) where n is the length of string2

def is_subsequence(string1, string2):
    """ Given two strings, find if first string is a subsequence of the second
        >>> print is_subsequence("AXY", "ADXCPY")
        True

        >>> print is_subsequence("AXY", "YADXCP")
        False

        >>> print is_subsequence("gksrek", "geeksforgeeks")
        True

    """

    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(string1):
        return True

    return False


def is_subsequence_recursive(string1, string2, m, n):
    """ Recursive solution to the above problem
        >>> print is_subsequence_recursive("AXY", "ADXCPY", 0, 0)
        True

        >>> print is_subsequence_recursive("AXY", "YADXCP", 0, 0)
        False

        >>> print is_subsequence_recursive("gksrek", "geeksforgeeks", 0, 0)
        True

    """

    if m == len(string1):
        return True

    if n == len(string2):
        return False

    if string1[m] == string2[n]:
        return is_subsequence_recursive(string1, string2, m + 1, n + 1)

    return is_subsequence_recursive(string1, string2, m, n + 1)



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print       



