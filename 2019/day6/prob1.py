
def recursive_orbits(node):
    #print(f'enter recursive_orbits for {node}')
    if len(node.children) == 0:
        return node.depth()
    child_orbits = 0
    for child in node.children:
        child_orbits += recursive_orbits(child)
    #print(f'{child_orbits + node.depth()} from {node} and below')
    return child_orbits + node.depth()

class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def depth(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.depth() + 1

    def __repr__(self):
        return self.name

graph = {}
seen = set()

'''
N59)FB6
COM)N59
'''
with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        parent_name, child_name = line.split(')')
        for node_name in [parent_name, child_name]:
            if node_name not in seen:
                node = Node(node_name)
                graph[node_name] = node
                seen.add(node_name)
        #print(f'adding child {child} to parent {graph[parent_name]}')
        graph[parent_name].add_child(graph[child_name])
        graph[child_name].set_parent(graph[parent_name])

root = graph['COM']
print(recursive_orbits(root))
