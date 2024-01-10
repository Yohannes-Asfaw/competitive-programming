class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def getanswer(bool1):
            left=0
            count=0
            ans=0
            for right in range(len(answerKey)):
                if answerKey[right]==bool1:
                    count+=1
                while count>k:
                    if answerKey[left]==bool1:
                        count-=1
                    left+=1
                ans=max(ans,right-left+1)
            return ans
        return max(getanswer("T"),getanswer("F"))
            
        