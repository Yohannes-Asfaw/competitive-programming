class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        ans1 = []
        ans2 = []
        for i in matches:
            winner = i[0]
            losser = i[1]

            if winner in d:
                d[winner][0] += 1
            else:
                d[winner] = [1, 0]
            
            if losser in d:
                d[losser][1] += 1
            else:
                d[losser] = [0, 1]

        for i in d:
            if d[i][1] == 0:
                ans1.append(i)

            elif d[i][1] == 1:
                ans2.append(i)

        ans1.sort()
        ans2.sort()

        return [ans1, ans2]