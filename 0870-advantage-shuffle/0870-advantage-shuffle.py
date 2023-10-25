class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort(reverse=True)
        nums2_index = [0 for _ in range(n)]
        for i in range(n):
            nums2_index[i] = (i, nums2[i])
        nums2_index.sort(key=lambda x: x[1], reverse=True)

        res = [0 for _ in range(n)]
        l = 0
        r = n-1
        for i, num in nums2_index:
            if nums1[l] > num:
                res[i] = nums1[l]
                l += 1
            else:
                res[i] = nums1[r]
                r -= 1
        
        return res
