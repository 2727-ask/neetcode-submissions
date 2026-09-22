class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        def backtrack(subset, i):
            if(i >= len(nums)):
                ans.add(tuple(sorted(subset.copy())))
                return
            
            subset.append(nums[i])
            backtrack(subset, i+1)
            subset.pop()

            backtrack(subset, i+1)

        backtrack([], 0)
        return [list(x) for x in ans] 

       