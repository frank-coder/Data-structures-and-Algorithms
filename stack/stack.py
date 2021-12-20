

class StackUsingList:
    def __init__(self) -> None:
        self.list = [1,2,3]

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

stc = StackUsingList()
print(stc.list[:-1])