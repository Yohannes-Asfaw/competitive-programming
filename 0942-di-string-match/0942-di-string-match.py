class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans=[]
        i=0
        j=len(s)
        for m in s:
            if m=="I":
                ans.append(i)
                i+=1
            else:
                ans.append(j)
                j-=1
        if s[len(s)-1]=="I":
            ans.append(j)
        else:
            ans.append(i)
        return ans
        
        






