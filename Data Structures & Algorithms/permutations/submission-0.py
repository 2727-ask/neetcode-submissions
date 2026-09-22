class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        


        ans = []

        used = [False]  * len(nums)

        def backtrack(subset):
            if(len(subset) == len(nums)):
                ans.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if(used[i]):
                    continue
                
                used[i] = True
                subset.append(nums[i])
                backtrack(subset)
                subset.pop()

                used[i] = False
            
        backtrack([])

        return ans