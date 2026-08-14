class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dp = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for x in s:
            if(len(stack) == 0):
                stack.append(x)
            else:
                top = stack[-1]
                if(top == dp.get(x)):
                    stack.pop()
                else:
                    stack.append(x)
        if(len(stack) != 0):
            return False
        return True