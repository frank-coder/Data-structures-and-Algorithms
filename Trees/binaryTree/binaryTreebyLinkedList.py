

class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    #print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

exampleTree = TreeNode("Drinks")
cold = TreeNode("Cold")
Hot = TreeNode("HOT")
fanta = TreeNode("Fanta")
coke = TreeNode("Coke")
tea = TreeNode("Tea")
cofee = TreeNode("Cofee")

exampleTree.leftChild = cold
exampleTree.rightChild = Hot

inOrderTraversal(exampleTree)
print("*" * 32)
preOrderTraversal(exampleTree)
print(exampleTree.leftChild.leftChild)