class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<=2:
            return False
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
                  

        index=0

        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                index=i
                break
        print(index)
        if index==0:
            return False
        elif arr[:index+1]==sorted(arr[:index+1]) and arr[index+1:]==sorted(arr[index+1:],reverse=True):
            return True
        else:
            return False
        