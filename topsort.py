from graph import Graph
from collections import defaultdict

class TopGraph(Graph):

    def topsort(self):
        return self._khan62()

    def _khan62(self):
        count = defaultdict(lambda :0)
        for node in self:
            for successor in self[node]:
                count[successor] += 1
    
        ready = [node for node in self if not count[node]]

        result = []

        while ready:
            node = ready.pop()
            result.append(node)
            for successor in self[node]:
                count[successor] -= 1
                if count[successor] == 0:
                    ready.append(successor)
        
        # If there's no cycles in the graph, then count will all be zero
        return result.reverse()

graph = TopGraph()

graph.add_arc(2)
graph.add_arc(3)
graph.add_arc(5)
graph.add_arc(7)
graph.add_arc(8)
graph.add_arc(9)
graph.add_arc(10)
graph.add_arc(11)

graph.add_edge(3, 8)
graph.add_edge(3, 10)
graph.add_edge(8, 9)
graph.add_edge(7, 11)
graph.add_edge(5, 11)
graph.add_edge(11, 9)
graph.add_edge(11, 2)
graph.add_edge(11, 10)
#graph.add_edge(9, 7)

#graph.add_edge(2,3)
#graph.add_edge(3,5)

graph.topsort()
