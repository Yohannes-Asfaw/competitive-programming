class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations=[num for num in range(1,n+1)]
        combs=[]
        # choose or not choose
        def binary(i,com):
            if len(com)==k:
                combs.append(com.copy())
                return 
            if i>=n:
                return 
            # include i this will be executed first of all time in the recursion
            com.append(combinations[i])
            binary(i+1,com) 
            com.pop()
            # not include i just continue
            binary(i+1,com)
        binary(0,[])
        return combs
       
            
