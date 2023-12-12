class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        print(list1)
        
        return " ".join(list1[::-1])