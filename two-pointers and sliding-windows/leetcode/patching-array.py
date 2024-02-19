class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered = 0
        i = 0
        answer = 0
        while i<len(nums) and covered < n:
            if nums[i] <= covered+1:
                covered+=nums[i]
                i+=1
            else:
                covered+=covered+1
                answer+=1
        while covered < n:
            covered+=covered+1
            answer+=1
        return answer

        