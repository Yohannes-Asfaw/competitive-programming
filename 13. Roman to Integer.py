def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10,'L':50,'C':100, 'D':500,'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90,'CD':400, 'CM':900}
        
        i, res = 0, 0
        
        while i < len(s):
            
            twoDig = s[i:i+2]
            oneDig = s[i]
            
            res += d[twoDig] if twoDig in d else d[oneDig]
            i += 2 if twoDig in d else 1

        
        return res
