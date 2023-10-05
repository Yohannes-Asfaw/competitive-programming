def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict()
        ans=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count.keys():
            if count[i]>(len(nums)/3):
                ans.append(i)
        return ans
