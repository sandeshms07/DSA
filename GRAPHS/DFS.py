from GRAPHS.graph import Graph


class DFS(Graph):
    def __init__(self, is_weighted_graph, is_directed_graph):
        super().__init__(is_weighted_graph, is_directed_graph)

    def traverse(self, entry_point=1):
        visit_order = []

        return visit_order


if __name__ == '__main__':
    val = DFS(False, False)
    print(val)
    print(val.traverse(5))
