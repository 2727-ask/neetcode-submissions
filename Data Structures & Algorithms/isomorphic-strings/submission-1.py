class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def convert(s):
            d = {}
            result = []
            num = 0

            for char in s:
                if char not in d:
                    d[char] = str(num)
                    num += 1

                result.append(d[char])

            return "".join(result)

        return convert(s) == convert(t)

         