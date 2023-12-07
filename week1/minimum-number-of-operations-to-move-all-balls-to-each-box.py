class Solution:
    def minOperations(self, boxes: str) -> List[int]:
      res=[]
      for box_ind in range(len(boxes)):
        r=0
        for ind in range(len(boxes)):
          if boxes[ind]=="1":
            r+=abs(ind-box_ind)
        res.append(r)
      return res