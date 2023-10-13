class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        check1=sorted(s1)
        i=0
        k=window
        while window<=len(s2):
            if check1==sorted(s2[i:window]):
                
                return True
            i+=1
            window+=1
        return False
        
        