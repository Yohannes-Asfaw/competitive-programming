class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt=Counter(t)
        counts=Counter()
        left=0
        ans=float("inf")
        res=""
        for right in range(len(s)):
            if s[right] in countt:
                counts[s[right]]+=1
            
            
            while left<len(s) and counts>=countt:
                if (right-left+1)<ans:
                    ans=right-left+1
                    res=s[left:right+1]
                    
                if s[left] in countt:
                    counts[s[left]]-=1
                left+=1
            
        return res
        
        