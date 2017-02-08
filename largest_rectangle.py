#O(n**2) time complexity
def largest_rectangle(heights,n):
    """There are  buildings in a certain two-dimensional landscape. Each building has a height given by .
     If you join  adjacent buildings, they will form a solid rectangle of area .
     Given  buildings, find the greatest such solid area formed by consecutive buildings.
        >>> print largest_rectangle([1, 2, 3, 4, 5],5)
        9

    """

    max_area = 0

    for i in xrange(n):
        min_height = heights[i]
        for j in xrange(i+1,n):
            if heights[j] < min_height:
                min_height = heights[j]
            area = (j - i + 1) * min_height
            max_area = max(max_area,area)
                
                       
    return max_area  


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print       
