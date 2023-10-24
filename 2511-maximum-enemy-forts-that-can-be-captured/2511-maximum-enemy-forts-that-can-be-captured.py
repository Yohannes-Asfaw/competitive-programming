class Solution:
    def captureForts(self, forts: List[int]) -> int:
        j=0
        ans=0
        while j<len(forts) and forts[j]!=-1 and forts[j]!=1:
            j+=1
        for i in range(j+1,len(forts)):
            if forts[i]!=0:
                
                if forts[j]==-forts[i]:
                    ans=max(ans,i-j-1)
                    j=i
                else:
                    j=i
            
        return ans

        