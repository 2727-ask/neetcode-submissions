class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # tokens = ["1","2","+","3","*","4","-"]


        for x in tokens:
            if(x not in '+-*/'):
                stack.append(int(x))
            else:
                two = stack.pop()
                one = stack.pop()
                if(x == '+'): 
                    stack.append(one + two)
                elif(x == '-'):
                    stack.append(one - two)
                elif(x == '*'):
                    stack.append(one * two)
                else:
                    stack.append(int(one / two))
        print(stack)
        return int(stack[-1])

