class MinStack:

    def __init__(self):
        self.stack=[]
        self.small=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.small:
            self.small.append(val)
        else:
            if self.small[-1]<=val:
                self.small.append(self.small[-1])
            else:
                self.small.append(val)


        

    def pop(self) -> None:
  
        self.stack.pop()
        self.small.pop()


        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.small[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()