class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        total_distinct=len(set(nums))
        freq={}
        left=0
        result=0
        for right in range(n):
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1
            while len(freq)==total_distinct:
                result+=n-right
                freq[nums[left]]-=1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left+=1
        return result
        
        