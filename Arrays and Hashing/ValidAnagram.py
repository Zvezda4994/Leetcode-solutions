class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        
        if len(s) != len(t):
            return False
        
        for l in t:
            if l not in counter or counter(l) == 0:
                return False
            counter(l) -= 1
        return True
            