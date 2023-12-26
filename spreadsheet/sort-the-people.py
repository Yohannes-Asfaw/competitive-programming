class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # ans=[]
        # for i in range(len(names)):
        #     ans.append([heights[i],names[i]])
        # ans=sorted(ans,reverse=True)
        # return [name for height,name in ans]
        dictionary={heights[i]:i for i in range(len(heights))}
        for i in range(len(heights)):
            min_idx = i
            for j in range(i+1, len(heights)):
                if heights[min_idx] > heights[j]:
                    min_idx = j        
            heights[i], heights[min_idx] = heights[min_idx], heights[i]

        ans=[]
        for i in heights:
            ans.append(names[dictionary[i]])

        return ans[::-1]
                
            