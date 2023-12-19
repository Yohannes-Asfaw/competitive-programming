class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        
        for path in paths:
            files = path.split(' ')
            directory = files[0]
            
            for file in files[1:]:
                name, content = file.split('(')
                dictionary[content[:-1]].append(directory + '/' + name)
                
        return [dictionary[content] for content in dictionary if len(dictionary[content]) > 1]