# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Minimal network
Problem 107
The following undirected network consists of seven vertices and twelve edges
with a total weight of 243.


The same network can be represented by the matrix below.

    A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-


However, it is possible to optimise the network by removing some edges and
still ensure that all from_points on the network remain connected. The network which
achieves the maximum saving is shown below. It has a weight of 93, representing
a saving of 243 − 93 = 150 from the original network.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file
containing a network with forty vertices, and given in matrix form, find the
maximum saving which can be achieved by removing redundant edges whilst
ensuring that the network remains connected.
"""
__sol__ = 259679
from collections import defaultdict


def minimal_network(network_lists):
    def connect(a, b):
        solution[a].add(b)
        solution[b].add(a)
        if a < b:
            del weights[(a, b)]
        else:
            del weights[(b, a)]

    def next_edges():
        return [(con, k) if k > con else (k, con) for k in solution.keys() for con in
                (connections[k]-set(solution.keys()))]

    def find_shortest_edge(next_edges=None):
        if next_edges is None:
            ret = min({k:v for k, v in weights.items()}, key=weights.get)
            return ret
        ret = min({k:v for k, v in weights.items() if k in next_edges}, key=weights.get)
        return ret

    solution = defaultdict(set)
    num_nodes = len(network_lists)
    network = [[int(network_lists[i][j])
                if network_lists[i][j] != '-' else 0
                for j in range(num_nodes)]
               for i in range(num_nodes)]
    connections = {i:{j for j in range(num_nodes) if network_lists[i][j] != '-'} for i in range(num_nodes)}
    weights = {(i, j):network[i][j] for j in range(num_nodes) for i in range(j) if network[i][j] > 0}

    # start with the shortest edge
    connect(*find_shortest_edge())

    # keep finding the shortest edge and adding to the solution
    while len(solution) < num_nodes:
        connect(*find_shortest_edge(next_edges()))

    reduced_weight = sum(v for k, v in weights.items())
    return reduced_weight


def p107():
    with open('../txt_files/p107_network.txt') as f: txt_lines = f.readlines()
    big_network = [line.strip('\n').split(',') for line in txt_lines]
    return minimal_network(big_network)


if __name__ == '__main__':
    ANSWER = p107()
    print("MAX SAVING: {}".format(ANSWER))
