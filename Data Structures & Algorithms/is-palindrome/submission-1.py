class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for x in s:
            if(x == " " or not x.isalpha() and not x.isnumeric()):
                clean = clean + ""
            elif(x.isnumeric()):
                clean = clean + f"{x}"
            else:
                clean = clean + x.lower()

        print(clean)
        return clean == clean[::-1]