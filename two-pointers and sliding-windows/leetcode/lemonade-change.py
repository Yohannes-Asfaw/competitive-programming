class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5=0
        count10=0
        for i in bills:
            if i==5:
                count5+=1
            elif i==10 and count5==0:
                return False
            elif i==10 and count5>=1:
                count10+=1
                count5-=1
            elif i==20 and count10==0 and count5<3:
                return False
            elif i==20 and count10>=1 and count5==0:
                return False
            elif i==20 and count10==0 and count5>=3:
                count5-=3
            elif i==20 and count10>=1 and count5>=1:
                count10-=1
                count5-=1
        return True

        