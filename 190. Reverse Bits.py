def reverseBits(self, n: int) -> int:
        res=0
        m=31
        for i in range(32):
            if n%2==1:
                res+=(2**(m-i))
            n=n//2

        return(res)
