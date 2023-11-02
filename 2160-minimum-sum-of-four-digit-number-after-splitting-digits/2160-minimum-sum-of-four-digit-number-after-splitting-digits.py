class Solution:
    def minimumSum(self, num: int) -> int:
        res = [int(x) for x in str(num)]
        res.sort()
        return int(str(res[0])+str(res[2]))+int(str(res[1])+str(res[3]))
        
 