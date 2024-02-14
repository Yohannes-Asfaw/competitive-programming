class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        ans=0
        div=len(costs)//2
        for i in range(len(costs)):
            if i<div:
                ans+=costs[i][0]
            else:
                ans+=costs[i][1]
        return ans
        