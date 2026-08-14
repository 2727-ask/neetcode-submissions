class Solution:
    def isHappy(self, n: int) -> bool:
        slow = total_sum(n)
        fast = total_sum(total_sum(slow))
        
        while(fast != 1):
            slow = total_sum(slow)
            fast = total_sum(total_sum(fast))
            
            if(slow == fast):
                return False 
        return True
        
def total_sum(n):
    if(n == 0):
        return 0
    total = 0
    for x in str(n):
        total = total + int(x) ** 2
        
    return total


        
        
        