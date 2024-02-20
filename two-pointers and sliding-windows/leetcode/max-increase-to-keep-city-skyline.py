class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        dic={}
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                m=0
                check=[]
                for m in range(len(grid)):
                    check.append(grid[m][j])
                dic[(i,j)]=min(max(grid[i]),max(check))
        ans=0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if dic[(i,j)]>grid[i][j]:
                    ans+=dic[(i,j)]-grid[i][j]
        return ans
