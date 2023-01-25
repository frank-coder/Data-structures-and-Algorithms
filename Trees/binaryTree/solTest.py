class Treenode:
    def __init__(self,data,children = []):
        self.data = data
        self.children = children

    # def addChild(self,data,child= []):


import collections

freq = collections.Counter("ababcbab")
print(freq)
for i in freq:
    if freq[i] > 1:
        print(i)