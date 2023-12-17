class OrderedStream:

    def __init__(self, n: int):
        self.list1=[None]*n
        self.indexcount=0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey-=1
        self.list1[idKey]=value
        if idKey>self.indexcount:
            return []
        while self.indexcount <len(self.list1) and self.list1[self.indexcount]:
            self.indexcount+=1
        return self.list1[idKey:self.indexcount]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)