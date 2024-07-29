from pyrsistent import pmap, pvector, plist, s, pset
import atomos.atom as atom
import logic

app_state = atom.Atom(None)


def initialize_state(edges_filepath):
    """Reads edges from file, builds an adjacency list and resets the app state to
    the adjacency list. Returns the new app state."""
    with open(edges_filepath, 'r') as fp:
        file_str = fp.read()
        edges = logic.file_contents_to_edges(file_str)
        return app_state.reset(logic.edges_to_adjacency_list(edges))


def add_edge(edge):
    """Add new edge to the app state and return the new state"""
    global app_state
    return app_state.swap(logic.with_new_edge, edge)


def is_same_network(customer_a, customer_b):
    """Returns whether a and b belong to the same collision network"""
    return logic.is_same_network(customer_a, customer_b, app_state.deref())