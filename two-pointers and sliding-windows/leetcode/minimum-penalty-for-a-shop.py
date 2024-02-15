class Solution:
    def bestClosingTime(self, customers: str) -> int:
        totaly=customers.count("Y")
        countn=0
        county=0
        ans=[]
        for i in customers:
            ans.append(totaly-county+countn)
            if i=="Y":
                county+=1
            else:
                countn+=1
        ans.append(totaly-county+countn)
         
        minval=min(ans)
        mini=ans.index(minval)
        return mini
        