#O(n) time complexity using greedy approach and O(1) space complexity
def get_max_profit(stock_prices_yesterday):
    """Write an efficient function that takes stock_prices_yesterday 
       and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

       >>> print get_max_profit([10, 7, 5, 8, 11, 9])  
       6

       >>> print get_max_profit([4,8,3,5])
       4
    """

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires atleast two prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy *and* sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be *negative*--we'd return 0!

        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price    
        
        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit 
 

# O(n^2 runtime)
def my_function(runtime,movie_lengths):
    # write the body of your function here
    for i in xrange(len(movie_lengths) - 1):
        for j in xrange(i+1,len(movie_lengths)):
            movie1 = movie_lengths[i]
            if movie_lengths[j] == runtime - movie1:
                return True
    return False


# O(n) runtime and spacetime due to the set
def solution2(runtime,movie_lengths):
    """
        >>> print solution2(5,[2,4,6,1]) 
        True
    """
    movie_lengths_seen = set()

    for first_movie in movie_lengths:
        second_movie = runtime - first_movie
        if second_movie in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie)
    return False            




# O(n) time complexity and O(1) space complexity
def find_unique_delivery_id(delivery_ids):
    """ Given the list of IDs, which contains many duplicate integers and one unique integer, 
    find the unique integer.

        >>> delivery_ids = [2,5,6,3,3,2,6]
        >>> print find_unique_delivery_id(delivery_ids)
        5
    """

    unique_id = 0

    for delivery_id in delivery_ids:
        unique_id ^= delivery_id

    return unique_id
    

# O(n) runtime and O(1) space complexity
def max_product_of_3(nums):
    """ Given a list of integers, find the highest product you can get from three of the integers.

        >>> nums = [1, 10, -5, 1, -100]
        >>> print max_product_of_3(nums)
        5000
    """

    if len(nums) < 3:
        raise Exception("Less than 3 items!")


    highest = max(nums[0], nums[1])
    lowest = min(nums[0], nums[1])

    highest_product_of_2 = nums[0] * nums[1]
    lowest_product_of_2 = nums[0] * nums[1]

    highest_product_of_3 = nums[0] * nums[1] * nums[2]

    for current in nums[2:]:

        # Debugging
        # print "highest_product_of_3: ", highest_product_of_3
        # print "highest_product_of_2: ", highest_product_of_2
        # print "lowest_product_of_2: ", lowest_product_of_2
        # print "highest: ", highest
        # print "lowest: ", lowest


        highest_product_of_3 = max(highest_product_of_3, current * highest_product_of_2, current * lowest_product_of_2) 

        highest_product_of_2 = max(highest_product_of_2, current * highest, current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2, current * highest, current * lowest)

        highest = max(highest, current)

        lowest = min(lowest, current)

    return highest_product_of_3    



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed! GOOD WORK!"
    print    

