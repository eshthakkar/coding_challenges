def print_tri(n):

    i = 1
    while(i<n):
        print 
        for j in xrange(i):
            print "*",
        i += 1 
    print    
    print "*"   

print_tri(11)    

def print_triangle(n):
    """Print triangle of n numbers in a given format"""
    
    i = 1
    count = 0
    while(count < n-1):
        print
        for j in xrange(i):
            count += 1
            print count,
        i += 1   
    print     
    print n

print_triangle(11)
print_triangle(16)






def find_pair_sum(arr,target):
    """ find two elements which the sum is 11 , return the index that you found
        >>> a = [1,4,5,7,9]
        >>> find_pair_sum(a,11)
        [1, 3]
    """

    i = 0
    j = len(arr) - 1
    
    while(i < j):
        val = arr[i] + arr[j]
        
        if val == target:
            return [i,j]
        
        elif val < target:
            i += 1
            
        else:
            j -= 1
            
    return -1                
    
    
        
        



#please return the highest two scores person's name

def highest_2_scores(arr):
    my_list = []
    
    for name_score in arr:
        name,score = name_score.split(":")
        score = int(score)
        my_list.append((name,score))
        
    new = sorted(my_list,key=lambda x: x[1], reverse=True)
    print new[0][0] + " and " + new[1][0]


a = ['JOH:30','Anne:100', 'Mark:50']
highest_2_scores(a)


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print 
   
    
                    










