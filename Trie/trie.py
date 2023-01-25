class TrieNode:
    def __init__(self):
        self.children = {}
        # EOS means end of string
        self.eos = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})

            current = node
        current.eos = True
        print("successfully Inserted!")

    def searchString(self,word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.eos == True:
            return True
        else:
            return False 

