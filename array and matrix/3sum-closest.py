class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closeans=[float("inf"),0]
        
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]<target:
                    if closeans[0]>abs(nums[i]+nums[left]+nums[right]-target):
                        closeans[0]=abs(nums[i]+nums[left]+nums[right]-target)
                        closeans[1]=nums[i]+nums[left]+nums[right]
                    left+=1
                elif nums[i]+nums[left]+nums[right]>target:
                    if closeans[0]>abs(nums[i]+nums[left]+nums[right]-target):
                        closeans[0]=abs(nums[i]+nums[left]+nums[right]-target)
                        closeans[1]=nums[i]+nums[left]+nums[right]
                    right-=1
                else:
                    if closeans[0]>abs(nums[i]+nums[left]+nums[right]-target):
                        closeans[0]=abs(nums[i]+nums[left]+nums[right]-target)
                        closeans[1]=nums[i]+nums[left]+nums[right]
                    left+=1
                    right-=1
                    break
        return closeans[1]
                
        