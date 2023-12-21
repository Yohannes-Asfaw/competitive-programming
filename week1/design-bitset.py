class Bitset:

    def __init__(self, size: int):
        self.zeros=[0 for i in range(size)]
        self.ones=[1 for i in range(size)]
        self.countzeros=size
        self.countones=0
        self.size=size

        

    def fix(self, idx: int) -> None:
        if self.zeros[idx]==0:
            self.countzeros-=1
            self.countones+=1
        self.zeros[idx]=1
        self.ones[idx]=0
        

    def unfix(self, idx: int) -> None:
        if self.zeros[idx]==1:
            self.countzeros+=1
            self.countones-=1
        self.zeros[idx]=0
        self.ones[idx]=1
        
        

    def flip(self) -> None:
        self.zeros,self.ones=self.ones,self.zeros
        self.countones,self.countzeros=self.countzeros,self.countones
        

    def all(self) -> bool:
        return self.countones==self.size
        

    def one(self) -> bool:
        return self.countones>0
        

    def count(self) -> int:
        return self.countones
        

    def toString(self) -> str:
        ans=""
        for i in self.zeros:
            ans+=str(i)
        return ans
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()