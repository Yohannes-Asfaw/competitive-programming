class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        ans=0
        for box,units in boxTypes:
            if truckSize>box:
                ans+=box*units
                truckSize-=box
            else:
                ans+=truckSize*units
                break
        return ans