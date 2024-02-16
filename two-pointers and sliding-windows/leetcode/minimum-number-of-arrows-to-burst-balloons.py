class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count=0
        minmum=points[0][1]
        print(points)
        for i in range(len(points)):
            if points[i][0]>minmum:
                minmum=points[i][1]
                count+=1
            minmum=min(minmum,points[i][1])
        return count+1
        