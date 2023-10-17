class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums1=[]
        nums2=[]
        for i in nums:
            if i%2==0:
                nums1.append(i)
            else:
                nums2.append(i)
        return nums1+nums2