import sys

def get_distances(points):
    _, _, largest_x, largest_y = find_maxes(points)
    end = max(largest_x, largest_y)
    areas = {}
    for row in range(400):
        for column in range(400):
            coord = (column, row)
            closest_point = closest(coord, points)
            if closest_point:
                try:
                    areas[closest_point] += 1
                except KeyError:
                    areas[closest_point] = 1
    return areas

def find_maxes(points):
    smallest_x = min([ point[0] for point in points ])
    smallest_y = min([ point[1] for point in points ])
    largest_x = max([ point[0] for point in points ])
    largest_y= max([ point[1] for point in points ])
    return (smallest_x, smallest_y, largest_x, largest_y)

def manhattan(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def closest(coord, points):
    distances = {}
    for point in points:
        distance = manhattan(coord, point)
        distances[point] = distance
    distance_list = list(distances.values())
    shortest_distance = distance_list[0]
    for distance in distance_list[1:]:
        if distance < shortest_distance:
            shortest_distance = distance
    if distance_list.count(shortest_distance) > 1:
        return None
    for k, v in distances.items():
        if v == shortest_distance:
            return k

def on_edge(coord, points):
    smallest_x, smallest_y, largest_x, largest_y = find_maxes(points)
    if coord[0] in [smallest_x, largest_x]:
        return True
    elif coord[1] in [smallest_y, largest_y]:
        return True
    else:
        return False

def enclosed(coord, points):
    found_top_left, found_bottom_left, found_top_right, found_bottom_right = False, False, False, False
    for point in points:
        if point[0] < coord[0] and point[1] < coord[1]:
            found_top_left = True
        elif point[0] < coord[0] and point[1] > coord[1]:
            found_bottom_left = True
        elif point[0] > coord[0] and point[1] < coord[1]:
            found_top_right = True
        elif point[0] > coord[0] and point[1] > coord[1]:
            found_bottom_right = True
    #print(coord, found_top_left and found_bottom_left and found_top_right and found_bottom_right)
    return found_top_left and found_bottom_left and found_top_right and found_bottom_right

def largest_not_infinite(points):
    max_distance = 0
    areas = get_distances(points)
    #print(areas)
    for k, v in areas.items():
        #print(f'current max: {max_distance}. checking {k}, {v}')
        if v > max_distance and enclosed(k, points):
            max_distance = v
            max_point = k
            #print(f'current max_point: {max_point}')
    print(max_point)
    return max_distance
            
if __name__ == '__main__':
    points = set()
    infile = sys.argv[1]
    with open(infile) as fh:
        for line in fh:
            x, y = [ int(coord.strip()) for coord in line.split(',') ]
            points.add((x, y))
    print(largest_not_infinite(points))
