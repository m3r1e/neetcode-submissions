class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = []
        starters = []
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                starters.append(num)
        for num in starters:
            count = 0
            while num in num_set:
                count += 1
                num = num+1
            counts.append(count)
        if not counts:
            return 0
        else:
            return max(counts)