class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for x in s:
            if x.isalnum():
                clean += x.lower()

        return clean == clean[::-1]