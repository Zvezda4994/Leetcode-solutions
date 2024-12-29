from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count [ord(c) - ord('a')] += 1 # determine alphabet position relative to A (1) and increment it
                
            key = tuple(count) # use this frequency count as a key (converted to tuple so its hashable)
            anagrams_dict[key].append(s) # add current string to the list that corresponds with said key
        
        return list(anagrams_dict.values())