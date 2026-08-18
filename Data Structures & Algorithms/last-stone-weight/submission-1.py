class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-num for num in stones]
        heapq.heapify(nums)

        print(nums)

        ans = 0
        while(len(nums) > 1):
            stone1 = heapq.heappop(nums)
            stone2 = heapq.heappop(nums)

            ans = abs(stone1) + stone2
            heapq.heappush(nums, -ans)
        
        return -nums[0]