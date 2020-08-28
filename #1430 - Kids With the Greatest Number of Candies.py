class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        x= max(candies)
        candies_max= []
        i= 0
        
        while i< len(candies):
            candies_max.append((extraCandies + candies[i]) >= x)
            i+=1
            
        return candies_max
                