# Time to lookup a word from the set is O(1) and total runtime is O(2^n) where n is the length of the target word
# Added a cache set seen to not go over paths that have already returned false
def is_word_possible(vocab, target_word, start, seen=None):
    """ Check if the given word can be made out of the provided list of words
        >>> vocab = ["cats", "dogs"]
        >>> print is_word_possible(vocab, "catsdogs", 0)
        True

        >>> print is_word_possible(vocab, "tower", 0)
        False

        >>> print is_word_possible(vocab, "catstower", 0)
        False

        >>> new_vocab = ["to", "tow", "er"]
        >>> print is_word_possible(new_vocab, "tower", 0)
        True

        >>> print is_word_possible([], "aa", 0)
        False

        >>> v_vocab = ["a", "b", "c", "d"]
        >>> print is_word_possible(v_vocab, "abd", 0)
        True

        >>> print is_word_possible(v_vocab, "c", 0)
        True

        >>> print is_word_possible(v_vocab, "d", 0)
        True

        >>> print is_word_possible(v_vocab, "dc", 0)
        True

        >>> print is_word_possible(v_vocab, "ddddddcccccbbbbaaaaa", 0)
        True


    """

    vocab_set = set(vocab)

    if seen is None:
        seen = set()

    if not vocab_set:
        return False 

    if start == len(target_word):
        return True

    if target_word in vocab_set:
        return True    

    for i in xrange(0,len(target_word) - start + 1):

        # Debugging
        # print seen
        # print "start: ", start
        # print "i: " , i
        # print "Target_word_slice: " , target_word[start:start+i]

        if target_word[start:start + i] in vocab_set and start + i not in seen:
            if is_word_possible(vocab, target_word, start + i, seen):
                return True
            seen.add(start + i)    
    return False        


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print            









