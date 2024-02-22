class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        ans=0
        arr=arr+[float("-inf")]
        print(arr)
        for i in range(len(arr)):
            while stack and arr[i]<arr[stack[-1]]:
                index=stack.pop()
                popped=arr[index]
                k=-1
                if stack:
                    k=stack[-1]
                ans+=popped * (i - index)*(index - k)
            stack.append(i)
        return ans%(1000000000+7)
        