class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end = 'end'
        

    def addWord(self, word: str) -> None:
        Node = self.root
        for c in word:
            if c not in Node:
                Node[c] = {}
            Node = Node[c]
        Node[self.end] = True

    
    def search(self, word: str) -> bool:
        def dfs(j, Node):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":  # Wildcard handling
                    for child in Node.values():  # Explore all children
                        if isinstance(child, dict) and  dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in Node:
                        return False  # Character not found in the children
                    Node = Node[c]  # Move to the next node
            return self.end in Node  # Check if the current node marks the end of a word

        return dfs(0, self.root)  # Start the DFS search from the root children

