class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(n):
            if n==0:
                return [1]
            elif n==1:
                return [1,1]
            m=pascal(n-1)
            new=[m[0]]
            for i in range(1,len(m)):
                if i==len(m)-1:
                    new.append(m[i-1]+m[i])
                    new.append(m[i])
                else:
                    new.append(m[i-1]+m[i])
            return new
        return pascal(rowIndex)

        