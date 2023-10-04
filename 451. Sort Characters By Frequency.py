def frequencySort(self, s: str) -> str:
        count=Counter(s)
        count2 = sorted(count.items(), key=lambda x:x[1], reverse=True)
        ans=""
        for i in count2:
            ans+=i[1]*i[0]
        return ans
