class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = set()
        for x in nums:
            if(x in dp):
                return True
            dp.add(x)
            
        return False