class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def backtrack(subset, i):
            if(i >= len(nums)):
                return 

            if(sum(subset) == target):
                ans.append(list(subset))
                return

            if sum(subset) > target:
                return

           
            # print(subset)
            subset.append(nums[i])
            backtrack(subset, i)
            subset.pop()


            backtrack(subset, i+1)
        
        backtrack([], 0)
        return ans
            