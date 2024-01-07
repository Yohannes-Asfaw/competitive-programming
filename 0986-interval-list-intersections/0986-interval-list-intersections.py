class Solution:
    def intervalIntersection(self, firstlist: List[List[int]], secondlist: List[List[int]]) -> List[List[int]]:
        if len(firstlist)==0 or len(secondlist)==0:
            return []
        ans=[]
    
        for i in range(len(firstlist)):
            j=0
            while j<len(secondlist):
                if firstlist[i][1]>=secondlist[j][0] and firstlist[i][0]<=secondlist[j][1]:
                    ans.append([max(firstlist[i][0],secondlist[j][0]),min(firstlist[i][1],secondlist[j][1])])
                j+=1
        return ans
        