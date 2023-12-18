class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i=0
        j=0
        times=0
        while s[i:j] in s[j:]:
            if len(s[i:j])>0:
                times=len(s)//len(s[i:j])
            if s[i:j]*times==s:
                return True
            j+=1
        
        return False
        