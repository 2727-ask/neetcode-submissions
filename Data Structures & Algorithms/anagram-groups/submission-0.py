class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dp = {}
        for x in strs:
            s = "".join(sorted(x))
            if(dp.get(s) != None):
                dp[s].append(x)
            else:
                dp[s] = [x]
        ans = []
        for key, value in dp.items():
            ans.append(value)
        
        return ans
