class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        current_largest=nums[-1]
        total=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=current_largest:
                current_largest=nums[i]
                continue
            if nums[i]%current_largest==0:
                numberofreplacement=nums[i]//current_largest
                current_largest=nums[i]//numberofreplacement
            else:
                numberofreplacement=nums[i]//current_largest+1
                current_largest=nums[i]//numberofreplacement
            total+=numberofreplacement-1
        return total
