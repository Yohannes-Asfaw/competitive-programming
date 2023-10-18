class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # two pointers prelen and curlen representing the length of the same strings
        prelen=0
        curlen=1
        count=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curlen+=1
            else:
                prelen=curlen
                curlen=1
            if prelen>=curlen:
                count+=1
        return count
