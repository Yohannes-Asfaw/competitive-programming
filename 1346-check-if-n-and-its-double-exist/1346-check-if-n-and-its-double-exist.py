class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zerocount=arr.count(0)
        if zerocount>1:
            return True
        dic={x:i for i,x in enumerate(arr)}
        for m in arr:
            if m%2==0 and m!=0:
                if m//2 in dic or m*2 in dic:
                    return True
            elif m!=0:
                if m*2 in dic:
                    return True
        return False


        