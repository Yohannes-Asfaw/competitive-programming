class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxheights=0
        for i in range(1,len(points)):
            maxheights=max(maxheights,points[i][0]-points[i-1][0])
        return maxheights

        