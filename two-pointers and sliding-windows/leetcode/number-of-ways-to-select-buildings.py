class Solution:
    def numberOfWays(self, s: str) -> int:
        _01nes=0
        _10s=0
        countzeros=0
        countones=0
        ans=0
        for i in s:
            if i=='0':
                countzeros+=1
                _10s+=countones
                ans+=_01nes
                
            elif i=='1':
                countones+=1
                _01nes+=countzeros
                ans+=_10s
            
        return ans

        