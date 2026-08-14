class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for x in range(0,n+1):
            no = str(bin(x))
            count = 0
            for y in no:
                if(y == '1'):
                    count = count + 1
            ans.append(count)
        return ans



