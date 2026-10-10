class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        path = []
        result = []

        pad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def backtrack(index):
            if(index == len(digits)):
                if(path):
                    result.append("".join(path))
                return

            for letters in pad[digits[index]]:
                for letter in letters:
                    path.append(letter)
                    backtrack(index + 1)
                    path.pop()

        backtrack(0)
        return result 

            
            