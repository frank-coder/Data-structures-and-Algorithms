
class BinaryHeap:
    def __init__(self,size):
        self.customList = (size+1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1

def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def getHeapSize(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapsize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapsize+1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode,index,heaptype):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heaptype.lower() == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heaptype)
    elif heaptype.lower() == "max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heaptype)

def insertNode(rootNode,nodeValue,heaptype):
    if rootNode.heapsize + 1 == rootNode.maxsize:
        return "The Binary heap is Full!"
    rootNode.customList[rootNode.heapsize + 1] = nodeValue
    rootNode.heapsize += 1
    heapifyTreeInsert(rootNode,rootNode.heapsize,heaptype)
    return "Inserted Successfully"

def heapifyTreeExtract(rootNode,index,heaptype):
    leftIndex = index*2
    rightIndex = index*2 + 1
    swapChild = 0

    if rootNode.heapsize < leftIndex:
        return
    elif rootNode.heapsize == leftIndex:
        if heaptype == "min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index],rootNode.customList[leftIndex]  = rootNode.customList[leftIndex],rootNode.customList[index]
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index],rootNode.customList[leftIndex]  = rootNode.customList[leftIndex],rootNode.customList[index]
            return
    else:
        if heaptype == "min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index],rootNode.customList[swapChild]  = rootNode.customList[swapChild],rootNode.customList[index]

        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index],rootNode.customList[swapChild]  = rootNode.customList[swapChild],rootNode.customList[index]

        heapifyTreeExtract(rootNode,swapChild,heaptype)

def extractNode(rootNode,heaptype):
    if rootNode.heapsize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapsize]
        rootNode.customList[rootNode.heapsize] = None
        rootNode.heapsize -= 1
        heapifyTreeExtract(rootNode,1,heaptype)
        return extractedNode
def deleteEntireHeap(rootNode):
    rootNode.customList = None

newHeap = BinaryHeap(5)
insertNode(newHeap,6,"max")
insertNode(newHeap,7,"max")
insertNode(newHeap,8,"max")
insertNode(newHeap,9,"max")
insertNode(newHeap,10,"max")
levelOrderTraversal(newHeap)
# extractNode(newHeap,"max")

