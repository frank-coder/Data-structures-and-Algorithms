class Node:
    def __init__(self,data) -> None:
        #self.prev = None
        self.next = None
        self.data = data
    def __str__(self):
        return f"{self.data} -> {self.next}"

class linkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
 
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
            

    def addToHead(self,newNode):
        newN = newNode
        if self.head == None:
            self.head = newN
            self.tail = newN
        else:
            newN.next = self.head
            self.tail = self.head
            self.head = newN

w = Node(2)
m = Node(4)
e = linkedList()
e.addToHead(w)
e.addToHead(m)

print([x.data for x in e])

print()
            
