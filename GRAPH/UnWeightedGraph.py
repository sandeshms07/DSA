from GRAPH.AbstractGraph import AbstractGraph


class UnWeightedGraph(AbstractGraph):

    def __init__(self, is_directed_graph, file_name='input-graph.txt'):
        super().__init__(is_directed_graph)
        if file_name:
            self.create_from_file(file_name)

    def __create_edges_non_waited(self, key, value):
        if int(key) in self.matrix:
            self.matrix[int(key)].append(int(value))
        else:
            self.matrix[int(key)] = [int(value)]

    def create_from_file(self, file_name='input-graph.txt'):
        with open(file_name) as x:
            for line in x:
                if line.strip():
                    line = line.split(' ')
                    key = int(line[0].strip())
                    value = int(line[1].strip())
                    self.__create_edges_non_waited(key, value)
                    if not self.is_directed_graph:
                        key = line[1].strip()
                        value = line[0].strip()
                        self.__create_edges_non_waited(key, value)
        self.nodes = len(self.matrix.keys())


if __name__ == '__main__':
    val = UnWeightedGraph(False)
    print(val, val.traverse_bfs(1), val.traverse_dfs(1), sep='\n')
