def convertToTitle(self, columnNumber: int) -> str:
        pos=deque()
        while columnNumber>0:
            columnNumber,output=divmod(columnNumber-1,26)
            print(output)
            pos.appendleft(output)
        return("".join([chr(i+ord('A')) for i in pos]))
