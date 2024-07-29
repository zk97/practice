from pyrsistent import pmap, pvector, plist, s
from functools import reduce

def string_to_edge(s):
    """aParses a string and returns an edge (a list with two elements)
    Example:
    >>> string_to_edge("1 2")
    plist([1, 2])
    """
    return plist(int(x) for x in s.split(" "))


def file_contents_to_edges(s):
    """Parses a file content and returns the edges.
    Example:
    >>> file_contents_to_edges("20 88\n72 35\n81 35\n")
    pvector([plist([20, 88]), plist([72, 35]), plist([81, 35])])
    """
    return pvector(string_to_edge(line) for line in s.split("\n")[:-1])

def with_new_connections(adjacency_list, new_connections):
    """Accepts an adjacency list and a map of new connections. For each key in both
    maps, joins the two sets. Keys appearing in only one of the maps are kept
    unchanged.
    """
    return adjacency_list.update_with(lambda v1, v2: v1.update(v2),
                                      new_connections)


def with_new_edge(adjacency_list, edge):
    """Adds the connection represented by edge. Remember: the edge is
    bidirected, so both connections from a to b and from b to a must be added
    to the adjacency list.
    """
    return with_new_connections(adjacency_list,
                                pmap({edge[0]: s(edge[1]),
                                      edge[1]: s(edge[0])}))


def edges_to_adjacency_list(edges):
    """Returns a map where each key is a node and the value is the nodes directly
    linked to the node on the key.
    Example:
    >>> edges_to_adjacency_list(pvector([plist([20, 88]),
    ...                                  plist([72, 35]),
    ...                                  plist([81, 35])]))
    pmap({72: pset([35]), 20: pset([88]), 88: pset([20]), 81: pset([35]), 35: pset([72, 81])})
    """

    return reduce(with_new_edge, edges, pmap())

def is_same_network(a, b, adjacency_list, visited=s()):
    """Checks if nodes a and b are in the same network.
    Examples:
    >>> is_same_network(1, 2, pmap({1: pset([2]), 2: pset([1, 3]),
    ...                             3: pset([2]), 4: pset([])}))
    True
    >>> is_same_network(1, 3, pmap({1: pset([2]), 2: pset([1, 3]),
    ...                             3: pset([2]), 4: pset([])}))
    True
    >>> is_same_network(2, 4, pmap({1: pset([2]), 2: pset([1, 3]),
    ...                             3: pset([2]), 4: pset([])}))
    False"""

    if a in visited:
        return False
    elif a == b:
        return True
    else:
        for next_vertex in adjacency_list[a]:
            if is_same_network(next_vertex, b, adjacency_list, visited.add(a)):
                return True
        return False