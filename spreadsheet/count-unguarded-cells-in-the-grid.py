class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [["." for _ in range(n)] for _ in range(m)]
        for i, j in walls:
            grid[i][j] = "W"
        for gurd in guards:
            gurd1, gurd2 = gurd[0], gurd[1]+1
            while gurd2 < n and grid[gurd1][gurd2] == ".":
                grid[gurd1][gurd2] = "H"
                gurd2 += 1
            gurd2 = gurd[1]
            while gurd2 >= 0 and grid[gurd1][gurd2] == ".":
                grid[gurd1][gurd2] = "H"
                gurd2 -= 1
        for gurd in guards:
            gurd2, gurd1 = gurd[0]+1, gurd[1]
            while gurd2 < m and grid[gurd2][gurd1] in ".H":
                grid[gurd2][gurd1] = "V"
                gurd2 += 1
            gurd2 = gurd[0]
            while gurd2 >= 0 and grid[gurd2][gurd1] in ".H":
                grid[gurd2][gurd1] = "V"
                gurd2 -= 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==".":
                    res += 1
        return res
        