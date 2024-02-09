class Solution:
    def maxScore(self, s: str) -> int:
        countzeros=0
        countones=s.count('1')
        if countones==len(s) or countones==0:
            return len(s)-1
        ans=0
        count=0
        for i in s:
            if i == '0':
                countzeros+=1
            elif i=='1':
                countones-=1
            if count>=0 and count<len(s)-1:
                ans=max(ans,countzeros+countones)
            count+=1
        return ans
            
        