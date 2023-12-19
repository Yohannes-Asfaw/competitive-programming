class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary=defaultdict(int)
        ans=[]
        for domain in cpdomains:
            count,address=domain.split(" ")
            count=int(count)
            addresses=address.split('.')
            for i in range(len(addresses)):
                one=".".join(addresses[i:])
                dictionary[one]+=count
        for i,j in dictionary.items():
            ans.append(str(j)+" "+i)
        return ans



        