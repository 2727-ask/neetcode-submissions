class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def isValid(curr):
            check = 0
            for x in curr:
                if(x == ")"):
                    check = check - 1
                else:
                    check = check + 1
                if(check < 0):
                    return False
            if(check == 0):
                return True
            return False

        res = []
        def dfs(curr):
            if(len(curr) == 2*n):
                if(isValid(curr)):
                   res.append(curr)
                return 


            curr = curr + "("
            if(Counter(curr).get("(") <= n):
                dfs(curr)
            curr = curr[:-1]
            curr = curr + ")"
            if(Counter(curr).get(")") <= n):
                dfs(curr)
        
        dfs("")

        return res


