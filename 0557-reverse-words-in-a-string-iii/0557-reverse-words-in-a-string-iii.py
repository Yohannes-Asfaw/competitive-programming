class Solution:
    def reverseWords(self, s: str) -> str:
        check=s.split(" ")
        ans=[]
        for i in check:
            ans.append(i[::-1])
        return " ".join(ans)


            


