class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod *= nums[j]
            new.append(prod)
        return new