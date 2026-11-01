class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        top_nums = sorted(d, key=d.get, reverse=True)[:k]

        return top_nums