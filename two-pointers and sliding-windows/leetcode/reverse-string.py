class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rec(left,right):
            if left>=right:
                return
            s[left],s[right]=s[right],s[left]
            return rec(left+1,right-1)
        rec(0,len(s)-1)