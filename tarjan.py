"""Tarjan's algorithm for finding strongly connected components
http://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm
"""

from __future__ import print_function
from collections import deque, defaultdict
from graph import Graph

class TestGraph(Graph):

    def tarjan(self):
        
        paths = deque()
        path_nodes = set()
        scc = defaultdict(lambda:[])

        def strongconnect(node, index):
            node.index = index
            node.lowlink = index
            paths.append(node)
            path_nodes.add(node)

            #print("here",str(node),str(node.index),str(node.lowlink))
            for successor in self[node]:
                if successor.index is None:
                    strongconnect(successor, index+1)
                    node.lowlink = min(node.lowlink, successor.lowlink)
                elif successor in path_nodes:
                    # form a cycle
                    node.lowlink = min(node.lowlink, successor.index)
                #print(str(node),str(node.index),str(node.lowlink))

            if node.lowlink == node.index:
                while paths:
                    v = paths.pop()
                    scc[node].append(v)
                    path_nodes.remove(v)
                    if v == node:
                        break

        for node in self:
            if node.index is None:
                strongconnect(node, 0)

        return scc

class Node(object):
    index = None
    lowlink = None
    name = None
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return self.name

    def __eq__(self, node):
        return self.name == node.name

    def __cmp__(self, node):
        if self.name < node.name:
            return -1
        elif self.name == node.name:
            return 0
        return 1

graph = TestGraph()

def add_node(value):
    graph.add_arc(value)

def add_edge(a, b):
    graph.add_edge(a,b)


nodes = []
for i in range(8):
    node = Node(i)
    nodes.append(node)
    add_node(node)

for a,b in [(0, 1), (1, 2), (2, 0), (3, 2), (3, 1), (4, 2), (3, 6), (6, 3), (6, 4), (7, 6), (5, 4), (4, 5), (7, 7)]:
    add_edge(nodes[a], nodes[b])

#graph.show()
scc = graph.tarjan()

def pprint_scc(scc):
    for node in scc:
        print("-->".join([str(successor) for successor in scc[node]]))

pprint_scc(scc)
