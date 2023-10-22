class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        ans=""
        for i in s:
            if i in "aeiouAEIOU":
                l.append(i)
        for i in s:
            if i in "aeiouAEIOU":
                ans+=l.pop()
            else:
                ans+=i

        return(ans)
        
 
            
