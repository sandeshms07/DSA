from graph import Graph


class BSF(Graph):
    def __init__(self, is_weighted_graph, is_directed_graph):
        super().__init__(is_weighted_graph, is_directed_graph)

    def traverse(self, entry_point=1):
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
                    if visited_nodes[x - 1] == 0:
                        queue.append(x)
                        visited_nodes[x - 1] = 1
        return visit_order


if __name__ == '__main__':
    val = BSF(False, False)
    print(val)
    print(val.traverse(5))
