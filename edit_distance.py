def editDist(str1, str2, m, n):
    """ Find edit distance between 2 strings using dynamic programming
        >>> str1 = "sunday"
        >>> str2 = "saturday"
        >>> print editDist(str1, str2, len(str1), len(str2))  
        3

        >>> str1 = "memoization"
        >>> str2 = "pl"
        >>> print editDist(str1, str2, len(str1), len(str2))  
        11

        >>> str1 = ""
        >>> str2 = "cat"
        >>> print editDist(str1, str2, len(str1), len(str2))  
        3

        >>> str1 = "cat"
        >>> str2 = ""
        >>> print editDist(str1, str2, len(str1), len(str2))  
        3

        >>> str1 = ""
        >>> str2 = ""
        >>> print editDist(str1, str2, len(str1), len(str2))  
        0

    """
    # Create a table to store results of subproblems

    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            # if first string is empty, only option is to insert all
            # characters of second string
            if i == 0:
                dp[i][j] = j

            # if second string is empty, only option is to delete all
            # characters of first string    
            elif j == 0:
                dp[i][j] = i 

            # if last characters are same, then the previous operations hold
            # true for it    
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # if last characters are not same, consider all possibilities
            # and find minimum    
            else:
                dp[i][j] = 1 + min(dp[i][j-1],   # Insert
                                   dp[i-1][j],   # Remove
                                   dp[i-1][j-1]) # Replace
    return dp[m][n]                                  
                       

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
 
  