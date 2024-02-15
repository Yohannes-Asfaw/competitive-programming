class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0]!=1:
            arr[0]=1
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                continue
            elif arr[i-1]<arr[i]:
                arr[i]=arr[i-1]+1

        return max(arr)
        