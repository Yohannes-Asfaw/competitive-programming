class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def rec(x,n):
            if n==0:
                return 1
            ans=rec(x,n//2)
            ans*=ans
            ans%=((10**9)+7)
            if n%2==1:
                ans*=x
                ans%=((10**9)+7)
            return ans
        return rec(5,(n//2)+(n%2))*rec(4,n//2)%((10**9)+7)