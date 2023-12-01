class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        alp = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            d[order[i]]=alp[i]
        def check(s):
            strint=''
            for i in s:
                strint+=d[i]
            return strint
        for i in range(len(words)-1):
            if check(words[i])>check(words[i+1]):
                print(check(words[i]),check(words[i+1]))
                return False
        return True
        
        