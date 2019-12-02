import sys

def get_leaf_nodes(graph):
    keys = set()
    values = set()
    leaves = []
    for k, v_list in graph.items():
        keys.add(k)
        if len(v_list) == 0:
            leaves.append(k)
        else:
            for v in v_list:
                values.add(v)
    return list(values - keys) + leaves


def strip_step(graph, step_id):
    #print(f'stripping {step_id}')
    delete_keys = []
    for k, v in graph.items():
        try:
            v.remove(step_id)
        except ValueError:
            pass
        if len(v) == 0:
            delete_keys.append(k)
    #for k in delete_keys:
    #    del graph[k]
    return graph

if __name__ == '__main__':
    dependencies = {}
    infile = sys.argv[1]
    with open(infile) as fh:
        for line in fh:
            split = line.split()
            parent_id, child_id = split[1], split[7]
            try:
                dependencies[child_id].append(parent_id)
            except KeyError:
                dependencies[child_id] = [parent_id]
    order_str = ''
    while True:
        #print(order_str)
        leaves = get_leaf_nodes(dependencies)
        leaves.sort()
        print(leaves)
        try:
            next_step = leaves.pop(0)
        except IndexError:
            print(dependencies)
            sys.exit(1)
        dependencies = strip_step(dependencies, next_step)
        print(dependencies)
        order_str += next_step
        
