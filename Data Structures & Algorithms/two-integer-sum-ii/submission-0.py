class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        while(left < right):
            curr_sum = numbers[left] + numbers[right]
            if(curr_sum == target):
                return [left+1, right+1]
            if(curr_sum > target):
                right = right - 1
                continue
            if(curr_sum < target):
                left = left + 1
                continue
            
            
