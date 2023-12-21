class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenDict = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenDict[tokenId] = currentTime + self.timeToLive

        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenDict.keys() : 
            if self.tokenDict[tokenId] > currentTime : 
                self.tokenDict[tokenId] = currentTime + self.timeToLive
        
        
      
    def countUnexpiredTokens(self, currentTime: int) -> int:
        counter = 0
        for key in self.tokenDict.keys() : 
            if self.tokenDict[key] > currentTime : 
                counter += 1 
        return counter 
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)