class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count=defaultdict(int)
        s2count=defaultdict(int)
        
        for i in s1:
            s1count[i]+=1
        for i in range(len(s1)):
            s2count[s2[i]]+=1
        if s1count==s2count:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            s2count[s2[left]]-=1
            if s2count[s2[left]]==0:
                s2count.pop(s2[left])
            s2count[s2[right]]+=1
            if s1count==s2count:
                return True
            left+=1
        
        return False
            
        
        