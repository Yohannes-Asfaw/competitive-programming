class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dict1=Counter(arr)
        for i,j in dict1.items():
            if j>len(arr)/4:
                return i