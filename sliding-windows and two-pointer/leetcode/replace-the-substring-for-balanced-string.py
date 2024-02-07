class Solution:
    def balancedString(self, s: str) -> int:
        k = len(s)//4
        d = {'Q':0,'W':0,'E':0,'R':0}

        for c in s:
            d[c] += 1

        if d['Q'] == k and d['W'] == k and d['E'] == k and d['R'] == k:
            return 0

        ans = len(s)
        i = 0

        for j in range(len(s)):
            d[s[j]] -= 1

            while i < len(s) and d['Q'] <= k and d['W'] <= k and d['E'] <= k and d['R'] <= k:
                ans = min(ans, j-i+1)
                d[s[i]] += 1
                i += 1
        return ans


        

            
        