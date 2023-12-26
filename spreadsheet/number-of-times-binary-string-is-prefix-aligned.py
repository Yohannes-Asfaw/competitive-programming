class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ones=0
        maxindex=0
        count=0
        for i in flips:
            ones+=1
            maxindex=max(maxindex,i)
            if ones==maxindex:
                count+=1
        return count
        
        
        
        