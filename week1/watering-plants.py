class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=1
        cap=capacity
        for i in range(len(plants)-1):
            cap-=plants[i]
            if cap<plants[i+1]:
                steps+=(i+1)*2+1
                cap=capacity
            else:
                steps+=1
        return steps