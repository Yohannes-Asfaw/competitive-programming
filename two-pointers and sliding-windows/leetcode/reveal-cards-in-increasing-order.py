class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = deque()
        for elem in sorted(deck ,reverse=True):
            if result:
                prev = result.pop()
                result.appendleft(prev)
            result.appendleft(elem)
        return list(result)


        