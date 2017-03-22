# Overlapping rectangle problem, O(1) space and time complexity
def find_rectangular_overlap(rect1, rect2):
    """ Find and return the overlapping rectangle between given 2 rectangles"""

    x_overlap_start_pt , overlap_width = find_range_overlap(rect1["x_left"], rect1["width"], rect2["x_left"], rect2["width"])
    y_overlap_start_pt , overlap_height = find_range_overlap(rect1["y_bottom"], rect1["height"], rect2["y_bottom"], rect2["height"])

    # return null rectangle if there is no overlap
    if not overlap_width or not overlap_height:
        return {
                "x_left" : None,
                "y_bottom" : None,
                "width" : None,
                "height" : None
        }

    return {
            "x_left" : x_overlap_start_pt,
            "y_bottom" : y_overlap_start_pt,
            "width" : overlap_width,
            "height" : overlap_height
    } 


def find_range_overlap(point1, length1, point2, length2):
    """ find and return the overlapping start point and length"""

    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    if highest_start_point >= lowest_end_point:
        return (None, None)

    overlap_length = lowest_end_point - highest_start_point
    
    return (highest_start_point, overlap_length)           


rect1 = {
        "x_left" : 1,
        "y_bottom" : 5,
        "width" : 10,
        "height" : 4
}  

rect2 = {
        "x_left" : 5,
        "y_bottom" : 7,
        "width" : 8,
        "height" : 6
} 

rect3 = {
        "x_left" : 11,
        "y_bottom" : 5,
        "width" : 2,
        "height" : 4
} 

print find_rectangular_overlap(rect1, rect2)
# Expected answer 
# {'width': 6, 'y_bottom': 7, 'x_left': 5, 'height': 2}  
print find_rectangular_overlap(rect1, rect3)
# Expected answer
# {'width': None, 'y_bottom': None, 'x_left': None, 'height': None} 
