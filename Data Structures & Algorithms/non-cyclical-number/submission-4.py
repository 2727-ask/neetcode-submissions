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
    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10

    return total


        
        
        