# Recursive solution with O(2**n) time complexity in worst case and worst case happens when all characters of X and Y mismatch i.e., length of LCS is 0.
def lcs(a, b, m, n):
    """Return the longest common subsequence for strings a and b
        >>> a = "AGGTAB"
        >>> b = "GXTXAYB"
        >>> print lcs(a, b, len(a), len(b)) 
        4

        >>> print lcs("","", 0, 0)
        0

        >>> a = "abcd"
        >>> b = "tfrrp"
        >>> print lcs(a, b, len(a), len(b))
        0

        >>> a = "abcd"
        >>> b = "tfdrrp"
        >>> print lcs(a, b, len(a), len(b))
        1

        >>> a = "abcd"
        >>> b = "afabbcd"
        >>> print lcs(a, b, len(a), len(b))
        4

    """

    if m == 0 or n == 0:
        return 0
    elif a[m-1] == b[n-1]:
        return 1 + lcs(a, b, m-1, n-1)
    else:
        return max(lcs(a, b, m-1, n), lcs(a, b, m, n-1))


# O(mn) time complexity although recursion is used due to memoization
def lcs_memoized(a, b, m, n):
    """Return the longest common subsequence for strings a and b
        >>> a = "AGGTAB"
        >>> b = "GXTXAYB"
        >>> print lcs_memoized(a, b, len(a), len(b)) 
        4

        >>> print lcs_memoized("","", 0, 0)
        0

        >>> a = "abcd"
        >>> b = "tfrrp"
        >>> print lcs_memoized(a, b, len(a), len(b))
        0

        >>> a = "abcd"
        >>> b = "tfdrrp"
        >>> print lcs_memoized(a, b, len(a), len(b))
        1

        >>> a = "abcd"
        >>> b = "afabbcd"
        >>> print lcs_memoized(a, b, len(a), len(b))
        4

    """
        
    cache = [[None for j in xrange(n+1)] for i in xrange(m+1)] 

    def lcs(a, b, m, n):
        if m == 0 or n == 0:
            if cache[m][n] == None:
                cache[m][n] = 0
            return cache[m][n]
        elif a[m-1] == b[n-1]:
            if cache[m-1][n-1] == None:
                cache[m-1][n-1] = lcs(a, b, m-1, n-1)

            return 1 + cache[m-1][n-1]
        else:
            if cache[m-1][n] == None:
                cache[m-1][n] = lcs(a, b, m-1, n)
            if cache[m][n-1] == None:
                cache[m][n-1] = lcs(a, b, m, n-1)
            return max(cache[m-1][n], cache[m][n-1])
    
    return lcs(a, b, m, n)                                       


# DP solution with O(mn) time complexity 
def longest_common_sub(a,b):
    """ Return the longest common subsequence for strings a and b
        >>> a = "AGGTAB"
        >>> b = "GXTXAYB"
        >>> print longest_common_sub(a, b)  
        4

        >>> print longest_common_sub("","")
        0

        >>> a = "abcd"
        >>> b = "tfrrp"
        >>> print longest_common_sub(a, b)
        0

        >>> a = "abcd"
        >>> b = "tfdrrp"
        >>> print longest_common_sub(a, b)
        1

        >>> a = "abcd"
        >>> b = "afabbcd"
        >>> print longest_common_sub(a, b)
        4

    """

    m = len(a)
    n = len(b)

    k = [[0 for i in xrange(n+1)] for j in xrange(m+1)]

    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif a[i-1] == b[j-1]:
                k[i][j] = k[i-1][j-1] + 1
            else:
                k[i][j] = max(k[i-1][j],k[i][j-1])
    return k[m][n]  


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
