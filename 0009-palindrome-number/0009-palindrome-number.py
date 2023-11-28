class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        print(x[::2])
        return x==x[::-1]
        