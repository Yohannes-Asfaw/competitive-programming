class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all=[]
        def perm(permu):
            if len(permu)==len(nums):
                all.append(permu.copy())
                return 
            for i in range(len(nums)):
                if nums[i] not in permu:
                    permu.append(nums[i])
                    perm(permu)
                    permu.pop()
        perm([])
        return all

                

