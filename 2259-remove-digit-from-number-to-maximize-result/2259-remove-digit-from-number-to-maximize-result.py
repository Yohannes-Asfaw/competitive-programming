class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=[]
        for i in range(len(number)):
            if number[i]==digit:
                ans.append(number[:i]+number[i+1:])
        return max(ans)