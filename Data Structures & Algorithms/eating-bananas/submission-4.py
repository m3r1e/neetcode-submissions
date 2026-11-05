class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            if sum((p + k - 1) // k for p in piles) <= h:
                hi = k          
            else:
                lo = k + 1      
        return lo
            