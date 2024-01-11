class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window=len(cardPoints)-k
        sum1=sum(cardPoints[:len(cardPoints)-k])
        ans=sum1
        left=0
        for right in range(len(cardPoints)-k,len(cardPoints)):
            sum1+=cardPoints[right]
            sum1-=cardPoints[left]
            left+=1
            ans=min(ans,sum1)
        return sum(cardPoints)-ans
        