class Solution:
    def isHappy(self, n: int) -> bool:
        dp = set()
        curr_sum = n
 
        while(curr_sum != 1):
            curr_sum = total_sum(curr_sum)
            if(curr_sum in dp):
                return False 
            dp.add(curr_sum)
        
        return True
        
def total_sum(n):
    if(n == 0):
        return 0
    total = 0
    for x in str(n):
        total = total + int(x) ** 2
        
    return total


        
        
        