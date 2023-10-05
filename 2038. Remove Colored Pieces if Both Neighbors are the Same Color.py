 def winnerOfGame(self, colors: str) -> bool:
        maxa=0
        counta=0
        maxb=0
        countb=0
        for i in colors:
            if i=="A":
                counta+=1
                countb=0
                maxa=max(counta,maxa)
                if counta>=3:
                    maxa+=counta
            else:
                countb+=1
                counta=0
                maxb=max(countb,maxb)
                if countb>=3:
                    maxb+=countb
        if maxa-2<=0:
            return False
        elif maxa-2>maxb-2:
            return True
        else:
            return False
