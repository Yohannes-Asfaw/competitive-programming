class Solution:
    def splitNum(self, num: int) -> int:
        numstr=sorted(str(num))
        num1=""
        num2=""
        for i in range(0,len(numstr),2):
            num1+=numstr[i]
        for i in range(1,len(numstr),2):
            num2+=numstr[i]
        return int(num1)+int(num2)