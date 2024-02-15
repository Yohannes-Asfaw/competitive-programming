class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        res = 0
        right = 0
        left = 0
        freq = {}
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i] = 0
            else:
                nums[i] = 1
        while right < len(nums):
            res+=nums[right]
            if res == k:
                ans+=1
            ans+=freq[res-k] if res - k in freq else 0
            freq[res] = freq.get(res,0)+1
            right+=1
        return ans