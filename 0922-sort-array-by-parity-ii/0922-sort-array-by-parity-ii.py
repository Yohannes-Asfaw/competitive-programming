class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds=[]
        even=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odds.append(i)
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even.pop()
            else:
                nums[i]=odds.pop()
        return nums
