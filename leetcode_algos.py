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


def find_all_concatenated_words(words):
    """ Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words."""

    words_set = set(words)
    ans = []

    def helper(w, curr, cnt):
        if curr == len(w):
            if cnt > 1:
                return True
            else:
                return False

        for i in xrange(curr + 1, len(w) + 1):
            if w[curr:i] in words_set and helper(w, i, cnt + 1):
                return True

        return False

    for w in words:
        if helper(w, 0, 0):
            ans.append(w)

    return ans  


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print find_all_concatenated_words(words)                                  


def find_concatenate_words(A):
    S = set(A)
    ans = []
    for word in A:
        print "word: ", word
        if not word: continue
        stack = [0]
        seen = {0}
        M = len(word)
        while stack:
            print "stack: ", stack
            print "seen: ", seen
            node = stack.pop()
            if node == M:
                ans.append(word)
                break
            for j in xrange(M - node + 1):
                if (word[node:node+j] in S and 
                    node + j not in seen and
                    (node > 0 or node + j != M)):
                    stack.append(node + j)
                    seen.add(node + j)


    return ans


print find_concatenate_words(words) 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print            