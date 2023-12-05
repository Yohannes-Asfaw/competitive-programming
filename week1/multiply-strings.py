class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a=0
        b=0
        number=-1
        for i,num in enumerate(num1):
            while str(number)!=num:
                number+=1
            a+=number*10**(len(num1)-1-i)
            number=-1
        for i ,num in enumerate(num2):
            while str(number)!=num:
                number+=1
            b+=number*10**(len(num2)-1-i)
            number=-1
        return str(a*b)
        