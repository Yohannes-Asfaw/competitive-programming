class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        minlen=0
        if len(word1)>=len(word2):
            minlen=len(word2)
        else :
            minlen=len(word1)
        i=0
        while i<minlen:
            ans+=word1[i]
            ans+=word2[i]
            i+=1
        if len(word1)>len(word2):
            ans+=word1[i:]
        else:
            ans+=word2[i:]
        return ans
                
        