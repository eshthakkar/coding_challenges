# O(n) time complexity and O(n) stack space
def get_permutations(string):
    """ Problem: Get all permutations of a string recursively and return them as a set
        >>> print sorted(list(get_permutations("cats")))
        ['acst', 'acts', 'asct', 'astc', 'atcs', 'atsc', 'cast', 'cats', 'csat', 'csta', 'ctas', 'ctsa', 'sact', 'satc', 'scat', 'scta', 'stac', 'stca', 'tacs', 'tasc', 'tcas', 'tcsa', 'tsac', 'tsca']

    """

    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last) 

    # put the last character in all possible positions for each of the above permutations
    permutations = set()
    for permutations_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in xrange(len(all_chars_except_last) + 1):
            permutation = permutations_of_all_chars_except_last[:position] + last_char + permutations_of_all_chars_except_last[position:]
            permutations.add(permutation)
            
    return permutations
    

if __name__ == "__main__":
    import doctest

    print

    result = doctest.testmod()

    if not result.failed:
        print "All tests passed! Gud work!"

    print    

