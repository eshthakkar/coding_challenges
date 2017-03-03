def remove_duplicates(nums):
    """Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this in place with constant memory.

    For example,
    Given input array nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

    >>> nums = [1, 1, 1]
    >>> remove_duplicates(nums)
    1

    >>> nums = [1, 1, 2]
    >>> remove_duplicates(nums)
    2

    >>> nums = []
    >>> remove_duplicates(nums)
    0

    """

    if not nums:
        return 0
            
    count = 0
    for i in xrange(1,len(nums)):
        if nums[i] != nums[count]:
            count += 1
            nums[count] = nums[i]
            
    return count + 1 

# O(n^2) runtime and O(n) space complexity
def find_sale_prices(sorted_prices):
    """ For instance, if the regular prices were 20, 80, and 100, the sale prices would be 
        15, 60, and 75,(which is 25 percent discount on regular price) and the printer's stack would consist of the labels 15, 20, 60, 75, 80, and 100.
        Return the sale prices from the printer's stack

        >>> nums = [15, 20, 60, 75, 80, 100]
        >>> print find_sale_prices(nums)
        [15, 60, 75]

        >>> nums = [9, 9, 12, 12, 12, 15, 16, 20]
        >>> print find_sale_prices(nums)
        [9, 9, 12, 15]

    """

    sale_prices = {}
    result = []

    for p in sorted_prices:
        sp = int(p * 0.75)
        if sp not in sale_prices:
            sale_prices[sp] = p
            
    for price in sorted_prices:
        if price in sale_prices:
            sorted_prices.remove(sale_prices[price])
            result.append(price)
    return result                


def group_anagrams(strs):
    """ Given an array of strings, group anagrams together.

        >>> words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        >>> print sorted(group_anagrams(words))
        [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
    """

    anagram_dict = {}
    for item in sorted(strs):
        sorted_item = ''.join(sorted(item))
        anagram_dict[sorted_item] = anagram_dict.get(sorted_item,[]) + [item]

    return anagram_dict.values()


# Time Complexity is O(n)
def sort_012(nums):
    """ 3 way partitioning problem, variation of famous Dutch national flag problem.
    Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[]. The functions should put all 0s first, then all 1s and all 2s in last.

    >>> nums = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    >>> print sort_012(nums)
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

    """

    low = 0
    mid = 0
    high = len(nums) - 1

    while (mid <= high):
        if nums[mid] == 0:
            if nums[low] != nums[mid]:
                nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            if nums[high] != nums[mid]:
                nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

    return nums        
                

def reverse_words(s):
    """ Reverse the words in a sentence without reversing the characters in a word
        >>> s = "the sky is blue"
        >>> print reverse_words(s)
        blue is sky the

        >>> s = "a"
        >>> print reverse_words(s)
        a

    """

    return ' '.join(s.split()[::-1])   


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print            