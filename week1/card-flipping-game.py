class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        minnumber=float("inf")
        check={}
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                check[fronts[i]]=i
        for i in range(len(fronts)):
            if fronts[i]!=backs[i]:
                if fronts[i] not in check: 
                    minnumber=min(minnumber,fronts[i])
                if backs[i] not in check:
                    minnumber=min(minnumber,backs[i])

        if minnumber==float("inf"):
            return 0
        return minnumber
        