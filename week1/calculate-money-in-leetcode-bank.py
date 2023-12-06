class Solution:
    def totalMoney(self, n: int) -> int:
        base=28
        week=n//7
        reminder=n%7
        ans=0
        for i in range(week):
            ans += (base+(7*i))
        for j in range(reminder):
            ans+=week+1+j
        return ans
            
        