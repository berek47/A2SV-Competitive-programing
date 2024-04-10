class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        names = ["Mary","John","Emma"]

        heights = [180,165,170]

        for i in range(len(heights)):
            for j in range(1,len(heights)):
                if height[i] < height[j] :
                    names[i],names[j] = names[j],names[i]              
        return names



        """
      
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                if heights[i] < heights[j] :
                    names[i],names[j] = names[j],names[i] 
                    heights[i],heights[j] = heights[j],heights[i]           
        return names
