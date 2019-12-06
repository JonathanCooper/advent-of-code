
def recursive_orbits(node):
    #print(f'enter recursive_orbits for {node}')
    if len(node.children) == 0:
        return node.depth()
    child_orbits = 0
    for child in node.children:
        child_orbits += recursive_orbits(child)
    #print(f'{child_orbits + node.depth()} from {node} and below')
    return child_orbits + node.depth()

def is_decendent(root, search_node):
    if root.name == search_node.name:
        return True
    elif len(root.children) == 0:
        return False
    for child in root.children:
        if child.name == search_node.name:
            return True
        if is_decendent(child, search_node):
            return True
    return False

def nearest_common_parent(node1, node2):
    while True:
        parent = node1.parent
        for child in parent.children:
            if is_decendent(child, node2):
                return parent
        return nearest_common_parent(parent, node2)

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

me = graph['YOU']
santa = graph['SAN']

common = nearest_common_parent(me, santa)
me_to_parent = me.parent.depth() - common.depth()
santa_to_parent = santa.parent.depth() - common.depth()
transfers = me_to_parent + santa_to_parent
print(transfers)
