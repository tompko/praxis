class Trie:
    def __init__(self):
        self.node = TrieNode()

    def add(self, value):
        if isinstance(value, str):
            self.node.add(value.lower())
        else:
            self.node.add(value)

    def __contains__(self, value):
        if isinstance(value, str):
            return value.lower() in self.node
        return value in self.node

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False
        
    def add(self, value):
        if len(value) == 0:
            self.end_node = True
        else:
            if value[0] not in self.children:
                self.children[value[0]] = TrieNode()
            self.children[value[0]].add(value[1:])

    def __contains__(self, value):
        if len(value) == 0:
            return self.end_node
        if value[0] in self.children:
            return value[1:] in self.children[value[0]]
        return False

def build_dictionary(path):
    dictionary = Trie()
    with open(path) as wordlist:
        for word in wordlist:
            dictionary.add(word.strip())
    return dictionary
