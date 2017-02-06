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



# Recursive solution, but has same computations over and over again due to overlapping subproblems. O(2^n) time complexity
def rod_cutting(rod_prices,n):
    """Returns the best obtainable price for a rod of length n and
       price[] as prices of different pieces

       >>> rod_prices = [1, 5, 8, 9, 10, 17, 17, 20]
       >>> n = len(rod_prices)
       >>> print rod_cutting(rod_prices,n)
       22
    """

    # Base case for recursion to stop
    if n <= 0:
        return 0

    max_price = 0

    # Recursively cut the rod in different pieces and compare different configurations
    for i in xrange(n):
        max_price = max(max_price,rod_prices[i] + rod_cutting(rod_prices,n-i-1))

    return max_price 


#O(n^2) time complexity using dynamic programming instead of O(2^n)
def rod_cut_dyn(prices,n):
    """Returns the best obtainable price for a rod of length n and
       price[] as prices of different pieces

       >>> rod_prices = [1, 5, 8, 9, 10, 17, 17, 20]
       >>> n = len(rod_prices)
       >>> print rod_cut_dyn(rod_prices,n)
       22
    """

    # A list of previously computed values
    val = [] 
    val.append(0)

    for i in xrange(1,n+1):
        max_val = 0
        for j in xrange(i):
            max_val = max(max_val, prices[j] + val[i-j-1])
        val.append(max_val)
    return val[n] 


def knapsack(W,val,wt,n):
    """0-1 knapsack problem
        >>> vals = [60, 100, 120]
        >>> wts = [10, 20, 30]
        >>> print knapsack(50,vals,wts,3)
        220
    """

    k = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i-1] <= w:
                k[i][w] = max(val[i-1] + k[i-1][w - wt[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
    return k[n][W]                
                           

                       

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
 
  