def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            if target - nums[i] in nums:
                answer.append(i)
                answer.append(nums.index(target - nums[i]))
                break
                return answer
