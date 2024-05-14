class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            print(node)
            for i, char in enumerate(word):
                if char == '.':
                    for child in node.children.values():
                        if dfs(child, word[i+1:]):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_word

        return dfs(self.root, word)

wordDictionary = WordDictionary()
result = wordDictionary.addWord("bad")
print(result)
result = wordDictionary.addWord("dad")
print(result)
result = wordDictionary.addWord("mad")
print(result)
result = wordDictionary.search("pad")
print(result)
result = wordDictionary.search("bad")
print(result)
result = wordDictionary.search(".ad")
print(result)
result = wordDictionary.search("b..")
print(result)

