class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=blocks[:k].count("W")
        ans=count
        left=0
        for right in range(k,len(blocks)):
            if blocks[right]=="W":
                count+=1
            if blocks[left]=="W":
                count-=1
            
            left+=1
            ans=min(count,ans)
        
        return min(ans,count)
            
                