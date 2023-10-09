def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        div=0
        res=[]
        while i>=0 or j>=0 or div:
            total=div
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total += int(b[j])
                j -= 1
            res.append(str(total%2))
            div=total//2
        return "".join(res[::-1])
