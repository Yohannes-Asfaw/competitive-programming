class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        list1=[]
        for i in range(len(s)+1):
            list1.append(0)
        for shift in shifts:
            if shift[2]==0:
                list1[shift[0]]-=1
                list1[shift[1]+1]+=1
            elif shift[2]==1:
                list1[shift[0]]+=1
                list1[shift[1]+1]-=1
        for i in range(1,len(list1)):
            list1[i]+=list1[i-1]
        ans=""
        for i in range(len(s)):
            ans+=chr((ord(s[i]) - ord("a") + list1[i]) % 26 + ord("a"))
        return (ans)
                
        