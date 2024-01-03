class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        initial=skill[i]+skill[j]
        chemistry=skill[i]*skill[j]
        i+=1
        j-=1
        
        while i<j:
            if skill[i]+skill[j]!=initial:
                return -1
            chemistry+=skill[i]*skill[j]
            i+=1
            j-=1
        return chemistry
        
        