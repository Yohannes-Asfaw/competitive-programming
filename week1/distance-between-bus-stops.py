class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        minindex=min(start,destination)
        maxindex=max(start,destination)
        return min(sum(distance[minindex:maxindex]),sum(distance[:minindex]+distance[maxindex:]))
        
            
        