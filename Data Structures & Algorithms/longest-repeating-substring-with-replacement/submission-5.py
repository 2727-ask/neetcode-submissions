class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        mymap = defaultdict(int)
        length = 0

        def getMostFrequentChar():
            mostfreq = 0
            for key, val in mymap.items():
                mostfreq = max(mostfreq, val)
            return mostfreq


        for right in range(len(s)):
            mymap[s[right]] += 1
            windowSize = right - left + 1 

            while(windowSize - getMostFrequentChar() > k and left < len(s)):
                mymap[s[left]] = mymap[s[left]] - 1
                left = left + 1
                windowSize = right - left + 1 
            
            length = max(length, windowSize)
        
        return length

            



