def get_middle_element(board):
    """
        >>> board = [[4, 1, 6, 4], [2, 4, 3, 7], [9, 10, 1, 5], [3, 3, 6, 8]]
        >>> print get_middle_element(board)
        (10, 2, 1)


        >>> board = [[4, 1, 6, 4, 2], [2, 4, 3, 7, 1], [9, 10, 1, 5, 0], [3, 3, 6, 8, 6]]
        >>> print get_middle_element(board)
        (3, 1, 2)

    """
    rows = len(board)
    cols = len(board[0])
    index_list = []

    # get middle indices/ index for rows
    if rows % 2 == 0:
        mid_row_index1 , mid_row_index2 = get_middle_indices(rows)
    else:
        mid_row_index = get_middle_indices(rows)


    # get middle indices/ index for cols
    if cols % 2 == 0:
        mid_col_index1 , mid_col_index2 = get_middle_indices(cols)
    else:
        mid_col_index = get_middle_indices(cols) 

    if rows % 2 == 0 and cols % 2 == 0:
        index_list = [(mid_row_index1, mid_col_index1), (mid_row_index1, mid_col_index2), (mid_row_index2, mid_col_index1), (mid_row_index2, mid_col_index2)]

    elif rows % 2 == 0: 
        index_list = [(mid_row_index1, mid_col_index), (mid_row_index2, mid_col_index)] 

    elif cols % 2 == 0:
        index_list = [(mid_row_index, mid_col_index1), (mid_row_index, mid_col_index2)]

    else:
        index_list = [(mid_row_index, mid_col_index)] 

    return max_element(index_list, board)                 


def max_element(index_list, board):
    max_row_index, max_col_index = 0, 0
    max_ele = 0

    for i in xrange(len(index_list)):
        current_row = index_list[i][0]
        current_col = index_list[i][1]

        if board[current_row][current_col] > max_ele:
            max_ele = board[current_row][current_col]
            max_row_index, max_col_index = current_row, current_col

    if max_element == 0:
        return (None, None, None)        

    return (max_ele, max_row_index, max_col_index)        


def get_middle_indices(total_elements):
    """ Return middle indices based on total elements being even or odd"""

    mid_index = int(total_elements/2)
    
    if total_elements % 2 == 0:
        return (mid_index, mid_index-1)

    return mid_index 


# Main problem function
def calculate_max_rides(board):
    """ Calculate the max no. of rides possible from the given mxn matrix starting from the middle of the board. Stop when all surrounding rides have been exhausted.
        You can move only in vertical and horizontal directions. 

        for e.g:
            board = 4 1 6 4
                    2 4 3 7
                    9 10 1 5
                    3 3 6 8

            starts at 10 from position (2, 1) and stops at position (0, 1) when the board looks like below:
            
            board = 0 0 0 0
                    0 0 0 0
                    0 0 1 0
                    0 0 0 0        

         >>> board = [[4, 1, 6, 4], [2, 4, 3, 7], [9, 10, 1, 5], [3, 3, 6, 8]]
         >>> print calculate_max_rides(board)
         75

    """

    # Get the middle start element, add it to the total rides and update board value at that position to 0
    middle_element, start_row, start_col = get_middle_element(board)
    total_rides = middle_element
    update_board(board, start_row, start_col)

    possible_moves_list =  possible_moves(board, start_row, start_col)
    current_element, current_row, current_col = max_element(possible_moves_list, board)


    while current_element:
        total_rides += current_element
        update_board(board, current_row, current_col)
        possible_moves_list =  possible_moves(board, current_row, current_col)
        current_element, current_row, current_col = max_element(possible_moves_list, board)

    return total_rides    


def update_board(board, row, col):
    """ Update the board at row, col index to value 0"""

    board[row][col] = 0
    # print_board(board)


def print_board(board):
    """ Print the board for debugging"""  

    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            print board[i][j],
        print      


def possible_moves(board, row, col):
    """ find the possible moves from current position in 4 directions

        >>> board = [[4, 1, 6, 4], [2, 4, 3, 7], [9, 10, 1, 5], [3, 3, 6, 8]]
        >>> print possible_moves(board, 2, 1)
        [(1, 1), (3, 1), (2, 0), (2, 2)]

        >>> print possible_moves(board, 0, 0)
        [(1, 0), (0, 1)]

    """

    possible_moves_list = []

    if row > 0:
        possible_moves_list.append((row - 1, col))

    if row < len(board) - 1:
        possible_moves_list.append((row + 1, col)) 

    if col > 0:
        possible_moves_list.append((row, col - 1))

    if col < len(board[0]) - 1:
        possible_moves_list.append((row, col + 1))    

    return possible_moves_list               


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print            
