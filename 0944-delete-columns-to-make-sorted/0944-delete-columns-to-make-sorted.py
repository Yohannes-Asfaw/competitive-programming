class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for j in range(len(strs[0])):
            check=[]
            for i in range(len(strs)):
                check.append(strs[i][j])
            if sorted(check)!=check:
                count+=1
        return count
