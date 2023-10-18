class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        list1=[i for i in range(len(s)) if s[i]==c]
        ans=[]
        j=0
        for i in range(len(s)):
            if s[i]==c:
                ans.append(0)
                j+=1
            elif i<list1[0]:
                ans.append(list1[0]-i)
            elif i>list1[-1]:
                ans.append(i-list1[-1])
            else:
                ans.append(min(list1[j]-i,i-list1[j-1]))
        return ans

        