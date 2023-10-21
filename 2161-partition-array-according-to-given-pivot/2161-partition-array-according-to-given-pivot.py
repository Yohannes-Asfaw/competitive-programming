class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        np=0
        for i in nums:
            if i==pivot:
                np+=1
            elif i<pivot:
                left.append(i)
            else:
                right.append(i)
        pivots=[pivot]*np
        return left+pivots+right
        