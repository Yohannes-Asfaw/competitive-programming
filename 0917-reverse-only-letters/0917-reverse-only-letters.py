class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        ans=[i for i in  s]
        while(j>i):
            if not ans[j].isalpha():
                j-=1
            if not ans[i].isalpha():
                i+=1
            if ans[i].isalpha() and ans[j].isalpha():
                ans[j],ans[i]=ans[i],ans[j]
                j-=1
                i+=1
        return "".join(ans)
            

