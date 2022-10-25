import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isEnd

trie = Trie()
trie.insert("qwerty")
trie.insert("qwsdfg")
trie.insert("qwsxcv")
trie.insert("zxcv")

print(trie.search("qwsdfg"))