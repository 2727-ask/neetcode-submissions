class Solution:
    def findMaxConsecutiveOnes(self, nums):
        current = 0
        maximum = 0

        for num in nums:
            if num == 1:
                current = current + 1
                maximum = max(maximum, current)
            else:
                current = 0

        return maximum