class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greaterthan=[]
        lessthan=[]
        equal=[]
        for i in nums:
            if i>pivot:
                greaterthan.append(i)
            elif i<pivot:
                lessthan.append(i)
                
            else:
                equal.append(i)
        return lessthan+equal+greaterthan