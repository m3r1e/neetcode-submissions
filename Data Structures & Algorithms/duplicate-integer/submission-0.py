class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         uniqueNums = []

         for i in nums:
            if i not in uniqueNums:
                uniqueNums.append(i)
            else:
                return True
         return False
        