anagrams = {}

def build_anagrams():
    with open("wordlist") as fin:
        for line in fin:
            word = line.strip().lower()
            if not word.isalpha():
                continue
            index = list(word)
            index.sort()
            index = "".join(index)
            anag_list = anagrams.get(index, set())
            anag_list.add(word)
            anagrams[index] = anag_list

build_anagrams()

def find_anagrams(word):
    index = list(word)
    index.sort()
    index = "".join(index)
    return anagrams[index]

def find_largest_class():
    biggest = []

    for val in anagrams.itervalues():
        if len(val) > len(biggest):
            biggest = val

    return biggest
