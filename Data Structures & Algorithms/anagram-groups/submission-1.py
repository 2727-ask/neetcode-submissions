class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            _map[key].append(word)

        ans = []
        for val in _map.values():
            ans.append(val)
        
        return ans