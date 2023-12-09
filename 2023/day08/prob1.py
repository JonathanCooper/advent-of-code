2
class Node(object):
    def __init__(self, name, left_child, right_child):
        self.name = name
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return f"{self.name} = ({self.left_child}, {self.right_child})"

class Graph(object):
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, left, right):
        self.nodes[name] = Node(name, left, right)

graph = Graph()

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        if line == "":
            continue
        elif "=" in line:
            name, children_info = line.split("=")
            name = name.strip()
            children_info = children_info.lstrip(" (").rstrip(")")
            left, right = children_info.split(", ")
            graph.add_node(name, left, right)
        else:
            instructions = line

current_node = graph.nodes["AAA"]
steps = 0

while True:
    instruction = instructions[steps % len(instructions)]
    steps += 1
    if instruction == "L":
        current_node = graph.nodes[current_node.left_child]
    elif instruction == "R":
        current_node = graph.nodes[current_node.right_child]
    else:
        raise ValueError(f"Unexpected instruction: {instruction}")
    if current_node.name == "ZZZ":
        print(steps)
        exit(0)

