class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n != 1:
            if n in check: 
                return False
            check.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return True
        