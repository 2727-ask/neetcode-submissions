class Solution:

    def encode(self, strs: List[str]) -> str:
        s = "" 
        if(len(strs) == 0):
            return '#o#'
        for x in range(len(strs)):
            if(x == len(strs) - 1):
                s = s + strs[x]
            else:
                s = s + strs[x] + "#_#"
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        if(s == "#o#"):
            return []
        return s.split('#_#')
