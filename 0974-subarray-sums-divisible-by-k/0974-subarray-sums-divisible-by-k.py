class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict=defaultdict(int)
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        count=0
        for i in nums:
            if i%k==0:
                count+=1
            if i%k in mydict:
                count+=mydict[i%k]
                mydict[i%k]+=1
            else:
                mydict[i%k]=1
        return count
        