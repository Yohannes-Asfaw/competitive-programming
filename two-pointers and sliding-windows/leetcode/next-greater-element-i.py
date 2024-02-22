class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={num:i for i,num in enumerate(nums1)}
        stack=[]
        ans=[-1 for i in range(len(nums1))]
        for i in nums2:
            while stack and i>stack[-1]:
                ans[dic[stack[-1]]]=i
                stack.pop()
            if i in dic:
                stack.append(i)
        return ans