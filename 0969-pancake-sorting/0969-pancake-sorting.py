class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        result=[]
        for i in range(len(arr)):
            maxindex=arr[0:n].index(max(arr[0:n]))
            result.append(maxindex+1)
            if maxindex!=0:
                arr[0:maxindex+1]=arr[0:maxindex+1][::-1]
            arr[0:n]=arr[0:n][::-1]
            result.append(n)
            n-=1
        return result
                