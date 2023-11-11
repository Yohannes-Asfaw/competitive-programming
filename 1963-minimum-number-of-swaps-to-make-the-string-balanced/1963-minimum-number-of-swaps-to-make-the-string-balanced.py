class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = 0
        stack = []
        for p in s:
            if p == "[": stack.append("[")
            else:
                if not stack: 
                    stack.append("]")
                    cnt += 1
                else: 
                    stack.pop()
        return cnt


                
            
