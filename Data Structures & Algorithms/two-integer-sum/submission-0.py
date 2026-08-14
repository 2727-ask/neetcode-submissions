class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if(dp.get(diff) != None):
                return [dp[diff], i]
            dp[nums[i]] = i



            