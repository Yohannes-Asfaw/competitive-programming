def lengthOfLastWord(self, s: str) -> int:
        count=" "
        for i in range(len(s)-1,-1,-1):
            if count[-1]!=" " and s[i]==" ":
                break
            elif s[i]!=" ":
                count+=s[i]
        return(len(count)-1)
