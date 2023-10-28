class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum1=sum(arr[:k])
        count=0
        if sum1/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            sum1+=arr[i]
            sum1-=arr[i-k]
            if sum1/k>=threshold:
                count+=1
        return count

            