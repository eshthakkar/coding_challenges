import sys

# Problem 1
def print_letters_in_triangle(n):
    """
        A
        A B
        A B C
        A B C D
        A B C D E
    """

    if n > 26:
        return

    for i in xrange(n):
        for j in xrange(i+1):
            sys.stdout.write(chr(ord('A') + j))
            if j < i:
                sys.stdout.write(" ")

        print


# Tests for the first problem
# for i in xrange(28):
#     print "n: %d" %i
#     print_letters_in_triangle(i)
#     print


def print_letters_starting_at_last(n):
    """
                E
              D E
            C D E
          B C D E 
        A B C D E  
    """

    if n > 26:
        return 

    for i in xrange(1,n+1):
        for j in xrange(n): 
            if (j < n-i): 
                sys.stdout.write(" ")
            else: 
                sys.stdout.write(chr(ord('A') + j))    

            if (j < n): 
                sys.stdout.write(" ")
        print           


# Tests for the second problem
# for i in xrange(28):
#     print "n: %d" %i
#     print_letters_starting_at_last(i)
#     print



def print_equilateral_triangle(n):
    """
                x     
              x x x
            x x x x x
          x x x x x x x 
        x x x x x x x x x  

    """

    for i in xrange(n):
        for j in xrange(2*n-1):
            if j < n - i - 1: 
                sys.stdout.write("  ")
            elif j < n + i - 1: 
                sys.stdout.write("x ")
            elif j < n + i: 
                sys.stdout.write("x")   
            else: 
                pass        
            
        print         
        


# print_equilateral_triangle(5)



def print_equilateral_triangle2(n):
    """
                x     
              x x x
            x x x x x
          x x x x x x x 
        x x x x x x x x x  
          x x x x x x x
            x x x x x 
              x x x
                x  
    """

    for i in xrange(n):      
        print_row(i, n)

    for i in xrange(n-2,-1,-1):
        print_row(i, n)         


def print_row(i, n):

    for j in xrange(2*n-1):
        if j < n - i - 1: 
            sys.stdout.write("  ")
        elif j < n + i - 1: 
            sys.stdout.write("x ")
        elif j < n + i: 
            sys.stdout.write("x")   
        else: 
            pass        
            
    print        


print_equilateral_triangle2(5)


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print         
    
