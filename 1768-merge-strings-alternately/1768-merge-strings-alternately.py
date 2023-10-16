class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=min(len(word1),len(word2))
        ans=""
        for i in range(len1):
            ans+=word1[i]
            ans+=word2[i]
        if len(word1)>len(word2):
                ans+=word1[len1:]
        else:
                ans+=word2[len1:]

        return ans
