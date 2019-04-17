def match_node(nodes, name):
    '''
    Returns the node whose name matches the specified name the most.
    '''
    name = name.lower()

    for node in nodes:
        node_name = node.name.lower()
        if name in node_name or node_name in name:
            return node

    raise NameError("Could not find a node with that name")

def distance(p1, p2):
    '''
    Returns the distance between two points
    '''
    return (
        (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    ) ** 0.5