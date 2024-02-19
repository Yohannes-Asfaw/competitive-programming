class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        ans=0
        for i,j in count.items():
            if j%2==0:
                ans+=j
            else:
                ans+=j-1
        if len(s)>ans:
            return ans+1
        return ans
