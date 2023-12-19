class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list1=list(s)
        i=0
        while i<len(s):
            list1[i:i+k]=list1[i:i+k][::-1]
            i+=2*k
        return "".join(list1)

            

        