class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        length = 0

        left = 0
        for right in range(len(s)):
            while(s[right] in myset):
                myset.remove(s[left])
                left = left + 1
            
            myset.add(s[right])
            length = max(length, right - left + 1)
        return length

                
