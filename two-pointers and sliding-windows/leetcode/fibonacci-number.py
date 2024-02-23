class Solution:
    def fib(self, n: int) -> int:
        def fibonachi(n):
            if n<=1:
                return n
            return fibonachi(n-1)+fibonachi(n-2)
        return fibonachi(n)
        
        