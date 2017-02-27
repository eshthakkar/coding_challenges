# O(n^2 + T) runtime where n is the total number of words and T is the total number of letters.
def max_product(words):
    """Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
       You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

       >>> print max_product(["ac","abb"])
       0

       >>> print max_product(["wtfn","abcde","abf"])
       20

    """

    max_product = 0
    bytes = [0] * len(words)

    for i in xrange(len(words)):
        val = 0
        for char in words[i]:
            val |= 1<<(ord(char) - ord('a'))
        bytes[i] = val

    for i in xrange(len(words)):
        for j in xrange(i+1,len(words)):
            if bytes[i] & bytes[j] == 0:
                max_product = max(max_product,len(words[i]) * len(words[j]))

    return max_product  

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
              



