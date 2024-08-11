from abc import ABC, abstractmethod


class AbstractGraph(ABC):
    def __init__(self, is_directed_graph):
        self.is_directed_graph = is_directed_graph
        self.nodes = 0
        self.is_waited_graph = False
        self.matrix = {}

    def traverse_bfs(self, entry_point):
        print(self.is_waited_graph)
        visited_nodes = []
        visit_order = []
        for x in range(0, self.nodes):
            visited_nodes.append(0)
        queue = []
        visited_nodes[entry_point - 1] = 1
        queue.append(entry_point)
        while queue:
            visited_node = queue.pop(0)
            adjacent_nodes = self.matrix.get(visited_node)
            visit_order.append(visited_node)
            if adjacent_nodes:
                for x in adjacent_nodes:
                    index = x[0] if self.is_waited_graph else x
                    if visited_nodes[index - 1] == 0:
                        queue.append(index)
                        visited_nodes[index - 1] = 1
        return visit_order

    @abstractmethod
    def traverse_dfs(self, entry_point):
        pass

    @abstractmethod
    def create_from_file(self, file_name):
        pass

    def __str__(self):
        data = ''
        for x in self.matrix.keys():
            data += str(x) + '=> ' + str(self.matrix.get(x)) + '\n'
        return "nodes = %s weighted = %s \n graph  = \n%s" % (
            self.nodes, self.is_waited_graph, data)
