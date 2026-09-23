class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)

        res_len = float("inf")
        res = [-1, -1]
        window = defaultdict(int)


        l = 0
        have = 0
        need_len = len(need)

        for r in range(len(s)):
            ch = s[r]

            window[ch] += 1

            if(ch in need and window[ch] == need[ch]):
                have = have + 1
            
            while(have == need_len):
                if(r - l + 1 < res_len):
                    res_len = r - l + 1
                    res = [l, r]

                
                left_char = s[l]
                window[left_char] = window[left_char] - 1

                if (left_char in need and window[left_char] < need[left_char]):
                    have = have - 1

                l = l + 1

        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

            


