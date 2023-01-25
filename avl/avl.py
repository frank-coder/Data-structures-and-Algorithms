class AVLNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rotateRight(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def rotateLeft(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue< rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild,nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild,nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rotateRight(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = rotateLeft(rootNode)
        return rotateRight(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return rotateLeft(rootNode)
    if balance < -1 and nodeValue <  rootNode.rightChild.data:
        rootNode.rightChild = rotateRight(rootNode)
        return rotateLeft(rootNode)
    return rootNode
    
def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode,nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rotateRight(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return rotateLeft(rootNode)
    if balance > 1 and getBalance(rootNode.rightChild) < 0:
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)

    return rootNode

def deleteAvl(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Avl deleted successfully"


    
newAvl = AVLNode(3)
newAvl = insertNode(newAvl,5)
newAvl = insertNode(newAvl,15)
newAvl = insertNode(newAvl,25)
newAvl = insertNode(newAvl,35)
newAvl = deleteNode(newAvl,5)

preOrderTraversal(newAvl)