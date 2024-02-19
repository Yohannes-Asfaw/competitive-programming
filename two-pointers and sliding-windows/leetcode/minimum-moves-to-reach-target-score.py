class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        while maxDoubles >0 and target>1:
            rem=target%2
            ans+=rem
            target=target//2
            ans+=1
            maxDoubles-=1
        ans+=target-1
        return ans

        