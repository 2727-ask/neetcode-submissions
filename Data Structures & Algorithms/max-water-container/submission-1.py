class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0 
        right = len(heights) - 1

        water = 0
        while(left <= right):
            minimum_height = min(heights[left],heights[right])
            length = right - left
            water = max(water, minimum_height * length)
            if(heights[left] <= heights[right]):
                left = left + 1
            else:
                right = right - 1
        
        return water

            
            
