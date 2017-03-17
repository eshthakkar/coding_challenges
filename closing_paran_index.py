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


def is_valid(code):
    """ Check if the paranthesis are correctly nested

        >>> code = "{ [ ] ( ) }"
        >>> print is_valid(code)
        True

        >>> code = "{ [ ( ] ) }"
        >>> print is_valid(code)
        False

        >>> code = "{ [ }"
        >>> print is_valid(code)
        False

    """

    st = []
    paran_vocab = {
                    "(" : ")",
                    "{" : "}",
                    "[" : "]" }

    openers = set(paran_vocab.keys())
    closers = set(paran_vocab.values())                

    for char in code:
        if char in openers:
            st.append(char)

        elif char in closers:

            if not st:
                return False

            else:
                last_seen_opener = st.pop()
                if not paran_vocab[last_seen_opener] == char:
                    return False

    return len(st) == 0                




if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print 

