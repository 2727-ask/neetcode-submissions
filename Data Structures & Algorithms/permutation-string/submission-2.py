class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l = 0
        r = len(s1)

        while(r <= len(s2)):
            window = Counter(s2[l:r])
            if(window == c1):
                return True
            l = l + 1
            r = r + 1
        return False


      