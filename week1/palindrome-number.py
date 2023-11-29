class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        print(x[::3])
        return x==x[::-1]
        