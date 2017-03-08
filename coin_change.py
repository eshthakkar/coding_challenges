# O(n*m) time and space complexity.
class Change(object):
    def __init__(self):
        self.memo = {}

    def coin_change(self, amt, coins, index):
        """ Return the number of ways in which amt of money can be made using the denomination provied
            >>> coins = [1, 2, 3]
            >>> test = Change()
            >>> print test.coin_change(4, coins, 0)
            4

            >>> test1 = Change()
            >>> print test1.coin_change(5, coins, 0)
            5
        """

        memo_key = str((amt,index))

        if memo_key in self.memo:
            return self.memo[memo_key]

        if amt == 0:
            return 1

        if index == len(coins):
            return 0    

        amt_with_coin = 0
        ways = 0

        while amt_with_coin <= amt:
            remaining_amt = amt - amt_with_coin
            ways += self.coin_change(remaining_amt, coins, index + 1)
            amt_with_coin += coins[index]

        self.memo[memo_key] = ways    

        return ways  


# Dynamic programming solution
# O(n*m) runtime and O(n) space complexity where n is amount of money and m is the number of potential denominations.
# Bottom up approach
def coin_change_dp(denominations, amount):
    """
        >>> coins = [1, 2, 3]
        >>> print coin_change_dp(coins, 4)
        4

        >>> print coin_change_dp(coins, 5)
        5
    """
    no_of_ways_n_cents = [0] * (amount + 1)

    # Base case
    no_of_ways_n_cents[0] = 1

    for coin in denominations:
        for higher_amt in xrange(coin, amount + 1):
            remainder_amt = higher_amt - coin
            no_of_ways_n_cents[higher_amt] += no_of_ways_n_cents[remainder_amt]

    return no_of_ways_n_cents[amount]        



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print        

