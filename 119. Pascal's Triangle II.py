 def getRow(self, rowIndex: int) -> List[int]:
        def Triangle(num):
            if num==0:

                return [1]

            else:
                prev=Triangle(num-1)
                res = []
                i=0
                j=1
                if len(prev)==1:
                    res.append(prev[i])
                    res.append(prev[j-1])
                    return res
                else:
                    while j<len(prev):
                        if i==0:
                            res.append(prev[i])
                        res.append(prev[i]+prev[j])
                        i+=1
                        if j==len(prev)-1:
                            res.append(prev[j])
                        j+=1

            return res
        return(Triangle(rowIndex))
