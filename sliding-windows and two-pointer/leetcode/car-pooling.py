class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        answer = [0] * (1001)

        for trip in trips:
            nump, fromi, twoi = trip
            answer[fromi] += nump
            answer[twoi] -= nump
            

        for i in range(1, 1001):
            answer[i] += answer[i-1]
        
        answer.pop()

        for i in answer:
            if i>capacity:
                return False
    

        return True 
        