class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(n):

            if n==0:
                return 1

            ans=pow(n//2)
            ans*=ans
            if n%2==1:
                ans*=x
            return ans
        

        if n>=0:
            return pow(n)
        return 1/pow(-1*n)
        
        