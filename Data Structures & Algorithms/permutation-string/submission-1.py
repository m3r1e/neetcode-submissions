class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        width = len(s1)
        s1 = sorted(s1)
        for i in range(len(s2)-width + 1):
            new = sorted(list(s2[i:i+width]))
            if new == s1:
                return True
        return False

            