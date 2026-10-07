class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        leftmax, rightmax = height[0], height[right]
        water = 0
        while(left < right):
            if(leftmax < rightmax):
                left = left + 1
                if(leftmax < height[left]):
                    leftmax = height[left]
                else:
                    water = water + (leftmax - height[left])
            else:
                right = right - 1
                if(rightmax < height[right]):
                    rightmax = height[right]
                else:
                    water = water + (rightmax - height[right])
                
        return water