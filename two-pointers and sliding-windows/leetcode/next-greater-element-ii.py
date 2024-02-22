class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        nums=nums+nums
        ans=[-1 for i in range(len(nums))]
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                ans[stack[-1]]=nums[i]
                stack.pop()
            stack.append(i)
        return ans[:len(ans)//2]
