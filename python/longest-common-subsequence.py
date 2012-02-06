def lcs(a, b):
    mat = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                mat[j+1][i+1] = mat[j][i] + 1
            else:
                mat[j+1][i+1] = max(mat[j][i+1], mat[j+1][i])

    return [a[i] for i in range(len(a)) if mat[-1][i] != mat[-1][i+1]]
