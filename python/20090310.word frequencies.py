import sys

def word_frequencies(path, n):
    frequencies = {}
    with open(path) as fin:
        for line in fin:
            for word in line.split():
                frequencies[word] = frequencies.get(word, 0) + 1

    sort_list = [(frequencies[w], w) for w in frequencies]
    sort_list.sort(reverse=True)
    return sort_list[:n]

if __name__ == "__main__":
    result = word_frequencies(sys.argv[1], int(sys,argv[2]))

    for r in result:
        print r[1], r[0]
