class TreeNode:
    def __init__(self,value,children = []) -> None:
        self.data = value
        self.children = children
        
    def __str__(self,level = 0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
            #print(child.__str__(level+1))
        return ret

    def addChild(self,treeNode):
        self.children.append(treeNode)

exampleTree = TreeNode("Drinks",[])
cold = TreeNode("Cold",[])
Hot = TreeNode("HOT",[])
exampleTree.addChild(cold)
exampleTree.addChild(Hot)
fanta = TreeNode("Fanta",[])
coke = TreeNode("Coke",[])
tea = TreeNode("Tea",[])
cofee = TreeNode("Cofee",[])

Hot.addChild(cofee)
Hot.addChild(tea)

cold.addChild(fanta)
cold.addChild(coke)

print(exampleTree)