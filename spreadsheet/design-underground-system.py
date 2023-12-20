class UndergroundSystem:

    def __init__(self):
        self.dictionary={}
        self.average=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dictionary[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.average[self.dictionary[id][0]+" to "+stationName].append(t-self.dictionary[id][1])
    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.average[startStation+" to "+endStation])/len(self.average[startStation+" to "+endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)