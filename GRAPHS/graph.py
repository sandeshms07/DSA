class Graph:
    nodes = 0
    edges = 0
    matrix = {}
    is_directed_graph = False
    is_waited_graph = False

    def __init__(self, is_waited_graph=False, is_directed_graph=False):
        self.is_directed_graph = False
        self.is_waited_graph = False
        self.nodes = 0
        self.edges = 0
        self.matrix = {}
        if is_waited_graph:
            self.construct_weighted_graph_from_file(is_directed_graph=is_directed_graph)
        else:
            self.construct_graph_from_file(is_directed_graph=is_directed_graph)

    def __create_edges_non_waited(self, key, value):
        if int(key) in self.matrix:
            self.matrix[int(key)].append(int(value))
        else:
            self.matrix[int(key)] = [int(value)]

    def __create_edges_weighted(self, key, value, weight):
        if int(key) in self.matrix:
            self.matrix[int(key)].append((int(value), int(weight)))
        else:
            self.matrix[int(key)] = [(int(value), int(weight))]

    def construct_graph_from_file(self, file_name='input-graph.txt', is_directed_graph=False):
        self.nodes = 0
        self.edges = 0
        self.matrix = {}
        is_first_line = True
        self.is_directed_graph = is_directed_graph
        with open(file_name) as x:
            for line in x:
                if line.strip():
                    line = line.split(' ')
                    if is_first_line:
                        is_first_line = False
                        self.nodes = int(line[0].strip())
                        self.edges = int(line[1].strip())
                    else:
                        key = int(line[0].strip())
                        value = int(line[1].strip())
                        self.__create_edges_non_waited(key, value)
                        if not is_directed_graph:
                            key = line[1].strip()
                            value = line[0].strip()
                            self.__create_edges_non_waited(key, value)

    def construct_weighted_graph_from_file(self, file_name='input-graph.txt', is_directed_graph=False):
        self.nodes = 0
        self.edges = 0
        self.matrix = {}
        is_first_line = True
        self.is_directed_graph = is_directed_graph
        self.is_waited_graph = True
        with open(file_name) as x:
            for line in x:
                if line.strip():
                    line = line.split(' ')
                    if is_first_line:
                        is_first_line = False
                        self.nodes = int(line[0].strip())
                        self.edges = int(line[1].strip())
                    else:
                        key = line[0].strip()
                        value = line[1].strip()
                        weight = line[2].strip()
                        self.__create_edges_weighted(key, value, weight)
                        if not is_directed_graph:
                            key = line[1].strip()
                            val = line[0].strip()
                            self.__create_edges_weighted(key, val, weight)

    def __str__(self):
        data = ''
        for x in self.matrix.keys():
            data += str(x) + '=> ' + str(self.matrix.get(x)) + '\n'
        return " edges = %s nodes = %s weighted = %s \n graph  = \n%s" % (
            self.nodes, self.edges, self.is_waited_graph, data)


if __name__ == '__main__':
    val = Graph(False, True)
    print(val)
    print('#####################')
    val2 = Graph(True, True)
    val2.construct_weighted_graph_from_file()
    print(val2)
