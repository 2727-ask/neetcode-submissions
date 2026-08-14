from collections import Counter

class Solution:
    def commonChars(self, words):
        common = Counter(words[0])

        for word in words[1:]:
            current = Counter(word)

            for char in common:
                common[char] = min(common[char], current[char])

        result = []

        for char, count in common.items():
            for _ in range(count):
                result.append(char)

        return result