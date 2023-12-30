#!/usr/bin/env python

def get_next_point(current, move):
    dir = move[0]
    dist = int(move[1:])
    if dir == 'U': # y-axis up
        return (current[0], current[1]+dist)
    if dir == 'D': # y-axis down
        return (current[0], current[1]-dist)
    if dir == 'R': # x-axis up
        return (current[0]+dist, current[1])
    if dir == 'L': # x-axis left
        return (current[0]-dist, current[1])
    print("Bad move", current, move)
    exit(-1)

def get_path(path_desc):
    current = (0,0)
    path = []
    moves = path_desc.split(',')
    for move in moves:
        next_point = get_next_point(current, move)
        path.append((current, next_point))
        current = next_point
    return path

def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def manhattan_dist(pt):
    return abs(pt[0])+abs(pt[1])

def get_intersection(seg_a, seg_b, a_dist, b_dist):
    # print seg_a, seg_b
    
    x_a_1, y_a_1 = seg_a[0]
    x_a_2, y_a_2 = seg_a[1]

    x_b_1, y_b_1 = seg_b[0]
    x_b_2, y_b_2 = seg_b[1]

    a_max_x = max(x_a_1, x_a_2)
    b_max_x = max(x_b_1, x_b_2)
    a_min_x = min(x_a_1, x_a_2)
    b_min_x = min(x_b_1, x_b_2)
    a_max_y = max(y_a_1, y_a_2)
    b_max_y = max(y_b_1, y_b_2)
    a_min_y = min(y_a_1, y_a_2)
    b_min_y = min(y_b_1, y_b_2)

    if a_max_x < b_min_x or b_max_x < a_min_x: # don't overlap on x axis
        return None
    if a_max_y < b_min_y or b_max_y < a_min_y: # don't overlap on y axis
        return None
    #TODO: Deal with lines that overlap for a while
    #print "Made it past overlap check"

    intersection = None
    # a is horizontal
    if x_a_1 == x_a_2:
        if y_b_1 != y_b_2:
            return None
        assert(min(y_a_1, y_a_2) <= y_b_1 <= max(y_a_1, y_a_2))
        intersection = (x_a_1, y_b_1)
    
    # a is vertical
    elif y_a_1 == y_a_2:
        if x_b_1 != x_b_2:
            return None
        assert(min(x_a_1, x_a_2) <= x_b_1 <= max(x_a_1, x_a_2))
        intersection = (x_b_1, y_a_1)
    else:
        print"Shouldn't get here", seg_a, seg_b
        exit(99)

    assert intersection is not None
    return a_dist+b_dist+distance(seg_a[0], intersection)+distance(seg_b[0], intersection)
    


# Now, read in the file and find all the intersections
with open('input.txt') as i:
    first_path = get_path(i.readline())
    second_path = get_path(i.readline())

shortest = 9999999999
a_so_far = 0
for a in first_path:
    b_so_far = 0
    for b in second_path:
        i = get_intersection(a, b, a_so_far, b_so_far)
        if i:
            #d = manhattan_dist(i)
            #if d > 0:
            shortest = min(i, shortest)
            print a, b
            print i, hortest
        b_so_far += distance(b[0], b[1])
    a_so_far += distance(a[0], a[1])
                

