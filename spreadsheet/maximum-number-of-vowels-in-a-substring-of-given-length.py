class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a':1,'e':1,'i':1,'o':1,'u':1}
        count=0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        ans=count
        left=0
        for right in range(k,len(s)):
            if s[right] in vowels:
                count+=1
            if s[left] in vowels:
                count-=1
            left+=1
            ans=max(ans,count)
        return ans
                
        