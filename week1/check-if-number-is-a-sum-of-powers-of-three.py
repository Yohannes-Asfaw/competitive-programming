class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            if n%3==2:
                return 0
            else:
                n//=3
        return True
        