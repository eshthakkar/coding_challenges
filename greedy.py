# O(n) time complexity

def activity_selector(activity):
    """Give a solution to choose maximum mutually independent activities that share a resource.
        Activities are initially sorted by their end times
    """

    max_array = [activity[0]]
    k = 0

    for i in xrange(1,len(activity)):
        if activity[i][0] >= activity[k][1]:  # Find next activity whose start time is greater than the previous max activity end time
            max_array.append(activity[i])
            k = i
    return max_array


activities = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]    
print activity_selector(activities)            