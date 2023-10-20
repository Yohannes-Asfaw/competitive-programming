class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            if bin(i) !=bin(i)[::-1]:
                return False
        return True 
        