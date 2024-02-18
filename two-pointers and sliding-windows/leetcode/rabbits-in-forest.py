class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)   
        num_rabbits = 0
        for val in count:
            if val == 0:
                num_rabbits += count[val]
            elif count[val] <= val + 1:
                num_rabbits += val + 1
            else:
                num_rabbits +=  (ceil(count[val]/(val+1)) * (val + 1))
        return num_rabbits