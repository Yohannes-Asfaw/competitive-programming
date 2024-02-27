class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo={}
        def score(left,right):
            if left>right:
                return 0
            if (left,right) in memo:
                return memo[(left,right)]
            score_of_taking_left=nums[left]-score(left+1,right)
            score_of_taking_right=nums[right]-score(left,right-1)
            memo[(left,right)]= max(score_of_taking_left,score_of_taking_right)
            return max(score_of_taking_left,score_of_taking_right)
            
        return score(0,len(nums)-1)>=0