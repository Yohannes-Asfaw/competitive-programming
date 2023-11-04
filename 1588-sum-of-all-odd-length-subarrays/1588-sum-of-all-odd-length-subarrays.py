class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                if (j-i)%2: ans += sum(arr[i:j])
        return ans
        