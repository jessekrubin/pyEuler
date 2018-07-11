# Solution to Python problem 107

## Solution code
```python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
G1






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
```

## Home made solution dependencies
