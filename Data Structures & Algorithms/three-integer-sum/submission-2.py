class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        #[-4,-1,-1,0,1,2]
        print(nums)
        ans = set()
        for i in range(len(nums)):
            target = nums[i] * -1
            left = i + 1
            right = len(nums) - 1
            while(left < right and right < len(nums)):
                curr_sum = nums[left] + nums[right]
                if(curr_sum == target):
                    ans.add((nums[i], nums[left], nums[right]))
                    right = right - 1
                    left = left + 1
                if(curr_sum > target):
                    right = right - 1
                    continue
                if(curr_sum < target):
                    left = left + 1
                    continue
        return [list(x) for x in ans]
                

                




            


        