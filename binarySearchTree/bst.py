from turtle import right


class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode,nodeData):
    if rootNode.data == None:
        rootNode.data = nodeData
    elif nodeData <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(nodeData)
        else:
            insertNode(rootNode.leftChild,nodeData)

    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(nodeData)
        else:
            insertNode(rootNode.rightChild,nodeData)

    return "Data has been inserted successfully!"


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
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


def searchNode(rootNode,value):
    if rootNode.data == value:
        print(f"Data found {rootNode.data}")
    elif value < rootNode.data:
        if rootNode.leftChild.data == value:
            print(f"Data found on Left: {rootNode.leftChild.data}")
        else:
            searchNode(rootNode.leftChild,value)

    else:
        if rootNode.rightChild.data == value:
            print(f"Data found on Right: {rootNode.rightChild.data}")
        else:
            searchNode(rootNode.rightChild,value)

def minValue(rootNode):
    current = rootNode
    while(rootNode.leftChild is not None):
        current = current.leftChild

    return current
def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,value)

    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
    return rootNode



newBst = BinarySearchTree(None)
insertNode(newBst,70)
insertNode(newBst,50)
insertNode(newBst,60)
insertNode(newBst,30)
insertNode(newBst,20)
insertNode(newBst,40)
insertNode(newBst,90)
insertNode(newBst,80)
insertNode(newBst,100)

# inOrderTraversal(newBst)
print(searchNode(newBst,70))


