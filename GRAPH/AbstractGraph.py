from abc import ABC, abstractmethod


class AbstractGraph(ABC):
    def __init__(self, is_directed_graph):
        self.is_directed_graph = is_directed_graph
        self.nodes = 0
        self.is_waited_graph = False
        self.matrix = {}

    @abstractmethod
    def traverse_dfs(self):
        pass

    @abstractmethod
    def traverse_bfs(self, entry_point):
        pass

    @abstractmethod
    def create_from_file(self):
        pass

    def __str__(self):
        data = ''
        for x in self.matrix.keys():
            data += str(x) + '=> ' + str(self.matrix.get(x)) + '\n'
        return "nodes = %s weighted = %s \n graph  = \n%s" % (
            self.nodes, self.is_waited_graph, data)

