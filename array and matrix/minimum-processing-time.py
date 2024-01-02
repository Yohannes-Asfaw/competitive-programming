class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans=-1
        for i, val in enumerate(processorTime):
            ans=max(ans,val+tasks[i*4])
        return ans
            