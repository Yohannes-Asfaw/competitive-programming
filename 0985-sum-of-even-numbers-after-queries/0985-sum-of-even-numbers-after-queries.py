class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum1=0
        ans=[]
        for i in nums:
            if i%2==0:
                sum1+=i
        for j in queries:
            if (nums[j[1]]+j[0])%2==0 and nums[j[1]]%2==0:
                sum1+=j[0]
                nums[j[1]]=nums[j[1]]+j[0]
                ans.append(sum1)
            elif (nums[j[1]]+j[0])%2!=0 and nums[j[1]]%2==0:
                sum1-=nums[j[1]]
                nums[j[1]]=nums[j[1]]+j[0]
                ans.append(sum1)
            elif (nums[j[1]]+j[0])%2==0 and nums[j[1]]%2!=0:
                sum1+=nums[j[1]]+j[0]
                nums[j[1]]=nums[j[1]]+j[0]
                ans.append(sum1)
            elif (nums[j[1]]+j[0])%2!=0 and nums[j[1]]%2!=0:
                ans.append(sum1)
                nums[j[1]]=nums[j[1]]+j[0]
        return ans
        