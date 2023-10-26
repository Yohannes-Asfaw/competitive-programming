class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        l=0
        count=0
        for i in range(k,len(s)+1):
            if len(s[l:i])==len(set(s[l:i])):
                count+=1
            l+=1
        return count
        
        