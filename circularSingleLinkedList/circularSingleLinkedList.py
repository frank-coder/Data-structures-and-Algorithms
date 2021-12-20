class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            

    def __repr__(self) -> str:
        lists = []
        current = self.head
        while current:
            if current == self.head:
                lists.append("Head: %s" %current.data)
            elif current == self.tail:
                lists.append("Tail: %s" %current.data)
            else:
                lists.append("%s" %current.data)

            current = current.next
            if current == self.tail.next:
                break
        return " -> ".join(lists)


    def createCSLL(self,newNode):
        node = Node(newNode)
        node.next = node
        self.head = node
        self.tail = node
        return "Circularsinglyll Created"

    def insertNode(self,newNode,pos) -> int:
        node = Node(newNode)
        if self.head is None:
            self.createCSLL(newNode)
            return
        if pos == 0:
            node.next = self.head
            #self.tail.next = node
            self.head = node
            self.tail.next = node
        elif pos == -1:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        else:
            index = 0
            tnode = self.head
            while index < pos -1:
                tnode = tnode.next
                index += 1
            nextNode = tnode.next
            tnode.next = node
            node.next = nextNode

        return
    def traverseCSLL(self):
        if self.head is None:
            return "Empty list"
        temp = self.head
        while temp:
            print(temp.data,end=",")
            temp = temp.next
            if temp == self.tail.next:
                print()
                break

    def searchCSLL(self,target):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:

            if temp.data == target:
                print(f"Seaarch target found: {temp.data}")
                break
            else:
                temp = temp.next
                if temp == self.tail.next:
                    print("Search target Not found")
                    break
        return 

    def deleteCSLL(self,target):
        if self.head is None:
            return "Empty List"
        if self.head == self.tail:
            self.head.next = None
            self.head = None
            self.tail = None
            return
        index = 1
        temp = self.head
        if target == 0:
            temp = self.head.next
            self.head = temp
            self.tail.next = temp

        elif target == -1:
            while temp is not None:
                if temp.next == self.tail:
                    break
                else:
                    temp = temp.next
            temp.next = self.tail.next
            self.tail = temp
            self.tail.next = temp.next
        else:
            while index < target -1:
                index += 1
                temp = temp.next
            temp.next = temp.next.next




csll = CircularSLL()
csll.createCSLL(21)
csll.insertNode(24,0)
csll.insertNode(23,1)
csll.insertNode(25,2)
csll.insertNode(25,1)
csll.insertNode(25,3)
csll.traverseCSLL()
csll.searchCSLL(21)
csll.deleteCSLL(-1)


print([x.data for x in csll])
print(csll)