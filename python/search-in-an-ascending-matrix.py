def search_matrix(matrix, item):
    i,j = 0, len(matrix[0]) - 1

    while matrix[i][j] != item:
        if matrix[i][j] < item:
            i += 1
        else:
            j -= 1

        if j < 0 or i >= len(matrix):
            return None
    return i,j
