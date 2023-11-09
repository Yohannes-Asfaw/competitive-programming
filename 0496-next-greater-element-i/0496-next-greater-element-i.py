class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numind={n:i for i ,n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
                val =stack.pop()
                indx=numind[val]
                res[indx]=cur
            if cur in numind:
                stack.append(cur)
        return res
                    
                