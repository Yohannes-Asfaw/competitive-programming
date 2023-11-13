class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while j>i:
            if s[j]!=s[i]:
                check1=s[i:j]
                check2=s[i+1:j+1]
                return check1==check1[::-1] or check2==check2[::-1]
            j-=1
            i+=1
        return True