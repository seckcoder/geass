from __future__ import print_function
from collections import defaultdict
class Graph(object):

    def __init__(self):
        self.adjacent = {}

    def add_arc(self, obj):
        self.adjacent.setdefault(obj, [])

    def add_edge(self, A, B):
        self[A].append(B)

    def __getitem__(self, node):
        return self.adjacent[node]

    def __iter__(self):
        return iter(self.adjacent)

    def show(self):
        visited = defaultdict(lambda: False)
        for node in self.adjacent:
            visited[node] = True
            print(node, end="")

            for successor in self[node]:
                visited[successor] = True
                print("-->"+str(successor), end="")

            print("\n")
