class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        return 

    def insert(self,value,position) -> int:
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if position == 0:
                newNode.next = self.head
                self.head = newNode
            elif position == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempN = self.head
                index = 0
                while index < position - 1:
                    tempN = tempN.next
                    index  += 1
                nextNode = tempN.next
                tempN.next = newNode
                newNode.next = nextNode

        return

    def traverseSLL(self):

        if self.head is None:
            print("Empty linked list")

        else:
            node = self.head
            while node.next != None:
                print(node.data)
                node = node.next

    def searchSLL(self,value):
        if self.head is None:
            print("List is empty")
            return
        else:
            node = self.head
            while node is not None:
                if node.data == value:
                    return f"Node found {node.data}"
                else:
                    node = node.next

            print("Object not found in the list")





singleLinkedList = SLinkedList()
n1 = Node(2)
n2 = Node(3)
tempLL = SLinkedList()
tempLL.add(21)
tempLL.add(23)
tempLL.add(25)
tempLL.insert(20,0)
tempLL.add(27)
tempLL.insert(19,0)
tempLL.searchSLL(5)



singleLinkedList.head = n1
singleLinkedList.head.next = n2
singleLinkedList.tail = n2

singleLinkedList.insert(1,1)
singleLinkedList.add(15)
singleLinkedList.insert(23,2)
print([_.data for _ in tempLL])
singleLinkedList.traverseSLL()
print(n2)