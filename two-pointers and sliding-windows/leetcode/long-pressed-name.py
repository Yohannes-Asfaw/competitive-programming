class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed)<len(name):
            return False
        i=0
        j=0
        while i<len(name):
            if j>=len(typed):
                return False
            if name[i]==typed[j]:
                i+=1
                j+=1
            elif i!=0 and name[i-1]==typed[j]:
                j+=1
            else:
                return False
        if j==len(typed):
            return True
        elif j<len(typed):
            while j<len(typed):
                if name[-1]!=typed[j]:
                    return False
                j+=1
            return True
        return False