class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        ans = []
        for x in digits:
            s = s + str(x)
            
        s = str(int(s) + 1)

        for x in s:
            ans.append(int(x))

        return ans

