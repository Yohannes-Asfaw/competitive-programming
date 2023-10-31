class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        seen={'a':0,
              'b':0,
               'c':0}
        count=0
        left=0
        for right in range(len(s)):
            seen[s[right]]+=1
            while seen['a'] and seen['b'] and seen['c']:
                count+=len(s)-right
                seen[s[left]]-=1
                left+=1
                
        return count
                
        