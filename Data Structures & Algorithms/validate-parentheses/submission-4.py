class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()


        for ch in s:
            top = stack[-1] if stack else None    
            if(ch == ")" and top == "("):
                stack.pop()
            elif(ch == "}" and top == "{"):
                stack.pop()
            elif(ch == "]" and top == "["):
                stack.pop()
            else:
                stack.append(ch)
        if(stack):
            return False
        return True
                
