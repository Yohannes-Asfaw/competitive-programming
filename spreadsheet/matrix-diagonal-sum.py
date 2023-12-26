class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum1=0
        i=0
        j=0
        while i!=len(mat) and j!=len(mat):
            sum1+=mat[i][j]
            i+=1
            j+=1
        a=0
        b=len(mat)-1
        while a !=len(mat) and b!=-1:
            sum1+=mat[a][b]
            a+=1
            b-=1
        if len(mat)%2==0:
            return sum1
        else:
            return sum1-mat[len(mat)//2][len(mat)//2]
        
        