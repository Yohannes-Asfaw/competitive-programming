class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            row=[]
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            ans.append(row)
        return ans
        