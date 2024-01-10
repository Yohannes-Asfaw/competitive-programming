class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        londstr = collections.defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            londstr[s[right]] += 1
            while londstr[s[right]]>1:
                londstr[s[left]] -= 1
                left+=1
            res = max(res, right - left + 1)
        return res