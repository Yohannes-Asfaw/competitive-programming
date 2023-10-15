class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]
        for j in range(len(image)):
            for m in range(len(image[0])):
                if image[j][m]==1:
                    image[j][m]=0
                else:
                    image[j][m]=1
        return image
