from GRAPH.AbstractGraph import AbstractGraph


class WeightedGraph(AbstractGraph):

    def __init__(self, is_directed_graph, file_name='input-graph.txt'):
        super().__init__(is_directed_graph)
        self.is_waited_graph = True
        if file_name:
            self.create_from_file(file_name)

    def traverse_dfs(self, entry_point):
        pass

    def create_from_file(self, file_name='input-graph.txt'):
        print(self.is_directed_graph)
        with open(file_name) as x:
            for line in x:
                if line.strip():
                    line = line.split(' ')
                    key = line[0].strip()
                    value = line[1].strip()
                    weight = line[2].strip()
                    self.__create_edges_weighted(key, value, weight)
                    if not self.is_directed_graph:
                        key = line[1].strip()
                        value = line[0].strip()
                        self.__create_edges_weighted(key, value, weight)
        self.nodes = len(self.matrix.keys())

    def __create_edges_weighted(self, key, value, weight):
        if int(key) in self.matrix:
            self.matrix[int(key)].append((int(value), int(weight)))
        else:
            self.matrix[int(key)] = [(int(value), int(weight))]


if __name__ == '__main__':
    val = WeightedGraph(True)
    print(val, val.traverse_bfs(5), sep='\n')
