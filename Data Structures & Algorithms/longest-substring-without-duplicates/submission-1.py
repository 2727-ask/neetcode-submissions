class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}

        left = 0 
        right = 0 
        maxi = 0
        curr = 0
        while(right < len(s)):
            if(s[right] in map):
                left = left + 1
                curr = 0
            map[s[right]] = 1
            curr = curr + 1
            maxi = max(maxi, curr)
            right = right + 1 
        return maxi
