from abc import ABC, abstractmethod


class AbstractGraph(ABC):
    def __init__(self, is_directed_graph):
        self.is_directed_graph = is_directed_graph
        self.nodes = 0
        self.is_waited_graph = False
        self.matrix = {}

    def traverse_bfs(self, entry_point):
        print(self.nodes)
        visited_nodes = [0] * self.nodes
        visit_order = []
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
                    if not visited_nodes[index - 1]:
                        queue.append(index)
                        visited_nodes[index - 1] = 1
        return visit_order

    def traverse_dfs(self, entry_point):
        visited_nodes = [False] * self.nodes
        visited_nodes[entry_point - 1] = True
        visiting_order = [entry_point]

        print(visited_nodes, 'visited nodes')
        self.__traverse(entry_point,visited_nodes,visiting_order )
        return visiting_order

    def __traverse(self, node, visited_nodes, visiting_order):
        for i in self.matrix.get(node):
            if not visited_nodes[i - 1]:
                visiting_order.append(i)
                visited_nodes[i - 1] = True
                self.__traverse(i, visited_nodes, visiting_order)

    @abstractmethod
    def create_from_file(self, file_name):
        pass

    def __str__(self):
        data = ''
        for x in self.matrix.keys():
            data += str(x) + '=> ' + str(self.matrix.get(x)) + '\n'
        return "nodes = %s weighted = %s \n graph  = \n%s" % (
            self.nodes, self.is_waited_graph, data)
