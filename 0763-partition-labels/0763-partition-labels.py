class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hasht={}
        for i,j in enumerate(s):
            hasht[j]=i
        end=0
        size=0
        res=[]
        for i,j in enumerate(s):
            size+=1
            end=max(end,hasht[j])
            if i==end:
                res.append(size)
                size=0
        return res
