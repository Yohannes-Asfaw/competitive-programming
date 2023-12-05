class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandie=max(candies)
        ans=[]
        for i in candies:
            if i+extraCandies >=maxcandie:
                ans.append(True)
            else:
                ans.append(False)
        return ans