class Solution:
    def printVertically(self, s: str) -> List[str]:
        list1=s.split()
        res=[]
        maxlen=0
        for i in list1:
            maxlen=max(maxlen,len(i))
        for i in range(maxlen):
            ans=[]
            for j in range(len(list1)):
                if i>=len(list1[j]):
                    ans.append(" ")
                else:
                    ans.append(list1[j][i])
            print(ans)
            res.append("".join(ans).rstrip())
        
        return res
        