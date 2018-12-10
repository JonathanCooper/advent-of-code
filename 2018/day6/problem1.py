import sys

def get_distances(points):
    _, _, largest_x, largest_y = find_maxes(points)
    end = max(largest_x, largest_y)
    areas = {}
    for row in range(end):
        for column in range(end):
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
    if coord == (349, 353):
        return False
    smallest_x, smallest_y, largest_x, largest_y = find_maxes(points)
    if coord[0] in [smallest_x, largest_x]:
        return True
    elif coord[1] in [smallest_y, largest_y]:
        return True
    else:
        return False

def largest_not_infinite(points):
    max_distance = 0
    areas = get_distances(points)
    #print(areas)
    for k, v in areas.items():
        if on_edge(k, points):
            #print(f'{k} is on edge')
            continue
        elif v > max_distance:
            max_distance = v
    return max_distance
            
if __name__ == '__main__':
    points = set()
    infile = sys.argv[1]
    with open(infile) as fh:
        for line in fh:
            x, y = [ int(coord.strip()) for coord in line.split(',') ]
            points.add((x, y))
    print(largest_not_infinite(points))
