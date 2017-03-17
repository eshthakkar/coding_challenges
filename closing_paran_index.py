# O(n) time and O(1) space
def get_closing_paran_index(sentence, open_paran_index):
    """ Return the closing paranthesis index from the input string

        >>> sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
        >>> print get_closing_paran_index(sentence, 10)
        79

        # Raises exception as expected
        # >>> sentence = "((tomorrow)"
        # >>> print get_closing_paran_index(sentence, 0) 
           

    """

    # start with the next character after the opening bracket
    position = open_paran_index + 1

    count = 0

    while position <= len(sentence) - 1:

        if sentence[position] == "(":
            count += 1

        elif sentence[position] == ")":

            if count == 0:
                return position

            else:
                count -= 1

        position += 1

    raise Exception("No closing paranthesis") 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print 

