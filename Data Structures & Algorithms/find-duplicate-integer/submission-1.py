class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        counter = Counter(nums)
        for key, val in counter.items():
            if(val > 1):
                return key