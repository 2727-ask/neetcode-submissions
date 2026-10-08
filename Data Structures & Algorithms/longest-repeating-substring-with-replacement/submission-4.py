class Solution:
    def characterReplacement(self, s, k):

        count = Counter()

        left = 0 
        result = 0
        maxfreq = 0 

        for right in range(len(s)):

            count[s[right]] = count[s[right]] + 1 
            maxfreq = max(maxfreq, count[s[right]])

            while((right - left + 1) - maxfreq > k):
                count[s[left]] = count[s[left]] - 1
                left = left + 1 
            
            result = max(result, right - left + 1)
        
        return result
