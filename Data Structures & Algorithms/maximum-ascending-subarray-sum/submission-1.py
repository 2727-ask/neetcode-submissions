class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mysum = 0
        for x in range(len(nums)):
            currsum = nums[x]
            for y in range(x + 1, len(nums)):
                if(nums[y - 1] < nums[y]):
                     currsum += nums[y]
                else:
                    break

               
            mysum = max(mysum,  currsum)  
        
        return mysum

            