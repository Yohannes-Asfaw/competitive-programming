class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtracking(i,curr,currsum):
            if currsum>target:
                return
            if currsum==target:
                res.append(curr.copy())
            for m in range(i,len(candidates)):
                curr.append(candidates[m])
                backtracking(m,curr,currsum+candidates[m])
                curr.pop()
        backtracking(0,[],0)
        return res

