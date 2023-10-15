class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            m=word.index(ch)
            ans=word[:m+1][::-1] + word[m+1:]  
            return ans
        else:
            return word
        
