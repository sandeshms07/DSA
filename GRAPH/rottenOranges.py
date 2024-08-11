data = [
    [2, 2, 2],
    [2, 1, 1],
    [2, 1, 1]
]


def calculate(rows, cols):
    max_time = 0
    rotten_nodes = []
    for x in range(0, rows):
        rotten_nodes.append([0] * cols)
    queue = []
    for row in range(0, rows):
        for col in range(0, cols):
            rotten_nodes[row][col] = data[row][col]
            if data[row][col] == 2:
                queue.append([row, col, 1])
    print('rotten_nodes', rotten_nodes)
    print('queue' , queue)
    drows = [0, 1, 0, -1]
    dcols = [1, 0, -1, 0]
    while queue:
        current = queue.pop(0)
        for x in range(0, 4):
            r = current[0] + drows[x]
            c = current[1] + dcols[x]
            if 0 <= r < rows and 0 <= c < cols:
                if (not rotten_nodes[r][c] == 2 and
                        not data[r][c] == 0):
                    print(r, c, current)
                    rotten_nodes[r][c] = 2
                    queue.append([r, c, current[2] + 1])
                    if max_time < current[2]:
                        max_time = current[2]
    print(rotten_nodes)
    for x in range(0, rows):
        for y in range(0, cols):
            if rotten_nodes[x][y] == 1:
                return -1
    return max_time





if __name__ == '__main__':
    print(calculate(3, 3))
