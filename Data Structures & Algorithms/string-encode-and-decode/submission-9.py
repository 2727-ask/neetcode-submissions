class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans = ans + s + "#_____#"
        return ans

    def decode(self, s: str) -> List[str]:
        return s.split("#_____#")[:-1]


