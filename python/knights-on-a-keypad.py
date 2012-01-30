neighbours = [[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]

def count(length):
    paths = [[-1 for i in range(10)] for j in range(length+1)]

    paths[1] = [1 for i in range(10)]

    for i in range(2, length+1):
        for j in range(10):
            paths[i][j] = sum([paths[i-1][n] for n in neighbours[j]])

    return paths[length][1]
