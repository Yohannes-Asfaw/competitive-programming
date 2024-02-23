class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = collections.deque()
        dire = collections.deque()
        for ind, char in enumerate(senate):
            radiant.append(ind) if char == 'R' else dire.append(ind)
        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.popleft()
                radiant.append(radiant.popleft() + len(senate))
            else:
                radiant.popleft()
                dire.append(dire.popleft() + len(senate))
        return 'Radiant' if radiant else 'Dire'
        