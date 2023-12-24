class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num="".join(map(str,digits))
        num2=str(int(num)+1)
        return list(map(int,list(num2)))
        