class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list1=[]
        for i in range(1,n+1):
            list1.append(i)
        i=-1
        while(len(list1)>1):
            print(list1)
            i+=k
            i=i%len(list1)
            list1.pop(i)
            i-=1
        return list1[0]

     
        