def pascal_triangle(n):
    row = [1]

    for i in range(n):
        print ' '.join([str(p) for p in row])
        row = [0] + row + [0]
        row = [row[i] + row[i+1] for i in range(len(row) - 1)]
