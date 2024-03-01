class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def comb(i,path):
            if len(path)==k:
                ans.append(path.copy())
            for j in range(i,n+1):
                path.append(j)
                comb(j+1,path)
                path.pop()
        comb(1,[])
        print(ans)
        return ans
            
