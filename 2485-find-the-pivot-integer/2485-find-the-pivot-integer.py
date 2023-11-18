class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        prefix1=[i for i in range(1,n+1)]
        sum1=sum(prefix1)
        for i in range(1,n):
            prefix1[i]+=prefix1[i-1]

        for i in range(1,len(prefix1)):
            if prefix1[i]==sum1-(prefix1[i-1]):
                return i+1
        return -1
            



        