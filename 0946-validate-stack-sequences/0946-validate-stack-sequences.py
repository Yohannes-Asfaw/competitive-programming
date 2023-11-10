class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack=[]
        j=0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1]==popped[j] and j<len(popped):
                j+=1
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False