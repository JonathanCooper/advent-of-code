
class Node(object):

    def __init__(self, name):
        self.name = name
        self.children = set()

    def add_child(self, child):
        self.children.add(child)

    def is_small(self):
        return self.name[0].islower()

    def __repr__(self):
        return self.name


def find_paths(node, path_so_far=None):
    #print(f'find_paths({node.name}, {path_so_far})')
    paths = 0
    if not path_so_far:
        path_so_far = []
    small_doubles = set()
    path_names = [ x.name for x in path_so_far ]
    #print(path_names)
    for seen in path_names:
        if not seen[0].islower():
            continue
        if path_names.count(seen) > 2:
            #print(f'too many {seen}')
            return 0
        elif path_names.count(seen) == 2:
            small_doubles.add(seen)
            if len(small_doubles) > 1:
                return 0
    if node.name == 'end':
        #print(f'hit end, path was {path_so_far + [node.name]}')
        return 1
    path_so_far.append(node)
    for child in node.children:
        paths += find_paths(child, path_so_far.copy())
    return paths

seen_cave_names = set()
caves = {}

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        #print(line)
        cave1, cave2 = line.split('-')
        if cave2 == 'start':
            cave1, cave2 = cave2, cave1
        if cave1 not in seen_cave_names:
            parent = Node(cave1)
            caves[cave1] = parent
            #print(f'{cave1} seen for first time')
        else:
            parent = caves[cave1]
        if cave2 not in seen_cave_names:
            child = Node(cave2)
            caves[cave2] = child
            #print(f'{cave2} seen for first time')
        else:
            child = caves[cave2]
        parent.add_child(child)
        #if parent.name == 'b':
            #for child in parent.children:
            #    print(f'b children:  {child.name}')
        if cave1 != 'start' and cave2 != 'end':
            child.add_child(parent)
        seen_cave_names.add(cave1)
        seen_cave_names.add(cave2)

num_paths = find_paths(caves['start'])
print(num_paths)
#b = caves['b']
#for child in b.children:
    #print(child.name)
