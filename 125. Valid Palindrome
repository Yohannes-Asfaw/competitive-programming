def isPalindrome(self, s: str) -> bool:
        s=list(s)
        for i in range(len(s)):
            if not s[i].isalnum():
                s[i]=""
            elif s[i].isalnum() and s[i].isupper():
                s[i]=s[i].lower()
        
        s="".join(s)
        print(s)

        return s==s[::-1]
