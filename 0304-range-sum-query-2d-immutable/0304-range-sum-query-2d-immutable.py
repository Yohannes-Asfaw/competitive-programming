class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        for i in range(1,len(matrix[0])):
            matrix[0][i]+=matrix[0][i-1]
        for i in range(1,len(matrix)):
            matrix[i][0]+=matrix[i-1][0]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.matrix[row2][col2]
        elif row1==0:
            return self.matrix[row2][col2]-(self.matrix[row2][col1-1])
        elif col1==0:
            return self.matrix[row2][col2]-(self.matrix[row1-1][col2])
            
        return self.matrix[row2][col2]-(self.matrix[row2][col1-1]+self.matrix[row1-1][col2])+self.matrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)