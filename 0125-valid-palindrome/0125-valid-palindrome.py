class Solution:
    def isPalindrome(self, s: str) -> bool:
        check=""
        for i in s:
            if i.isalnum():
                check+=(i.lower())
        print(check)
        i=0
        j=len(check)-1
        while i<j:
            if check[i]!=check[j]:
                return False
            i+=1
            j-=1
        return True
        