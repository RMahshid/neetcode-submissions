class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first solution
        return sorted(s) == sorted(t)

