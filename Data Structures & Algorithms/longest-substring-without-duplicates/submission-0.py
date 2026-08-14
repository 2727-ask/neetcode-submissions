class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        dp = set()
        max_length = 0
        for i in range(len(s)):
            while(s[i] in dp):
                dp.remove(s[left])
                left += 1

            dp.add(s[i])
            max_length = max(max_length, len(dp))


        return max_length
            