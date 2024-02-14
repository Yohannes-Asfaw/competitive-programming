class Solution:
    def minimumSteps(self, s: str) -> int:
        countones=s.count('1')
        index=len(s)-countones
        range1=index-1
        countzeros=s.count('0')
        index2=countzeros-1
        ans=0
        for i in range(range1):
            if s[i]=='1':
                ans+=index-i
                index+=1
        for i in range(len(s)-1,index2-1,-1):
            if s[i]=='0':
                ans+=i-index2
                index2+=1
        return ans


        

        