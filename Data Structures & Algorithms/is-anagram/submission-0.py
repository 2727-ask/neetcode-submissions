class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = Counter(s)
        mt = Counter(t)

        if(ms == mt):
            return True
        else:
            return False