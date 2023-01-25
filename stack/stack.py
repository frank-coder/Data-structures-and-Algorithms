

# class StackUsingList:
#     def __init__(self) -> None:
#         self.list = [1,2,3]
#         self.b = [0] * sum(self.list)

#     def __str__(self) -> str:
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return "\n".join(values)

# stc = StackUsingList()
# print(stc.b[:])

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        else:
            return self.minNode.value

    def push(self,value):
        if not self.top:
            self.top = Node(value)
            self.top.next = self.top
        else:
            self.top.next = self.top
            self.top = Node(value)
        if not self.minNode:
            #self.minNode.next = self.minNode
            self.minNode = Node(value)
        elif value < self.minNode.value:
            self.minNode = Node(value)



    def pop(self):
        if not self.top:
            return None
        if self.top.value <= self.minNode.value:
            self.minNode = self.minNode.next
        item = self.top
        self.top = self.top.next
        return item
              


s = Stack()
s.push(3)
s.push(6)
s.push(1)
s.push(7)
s.pop()
print(s.min())

print(s.top.next)