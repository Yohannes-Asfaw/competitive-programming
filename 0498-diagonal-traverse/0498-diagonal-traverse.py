class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        direction=0
        result=[]
        i,j=0,0
        for _ in range(m*n):
            result.append(mat[i][j])
            if direction==0:
                if j==m-1:
                    i+=1
                    direction=1
                elif i==0:
                    j+=1
                    direction=1
                else:
                    i-=1
                    j+=1
            else:
                if i==n-1:
                    j+=1
                    direction=0
                elif j==0:
                    i+=1
                    direction=0
                
                else:
                    i+=1
                    j-=1
        return result
