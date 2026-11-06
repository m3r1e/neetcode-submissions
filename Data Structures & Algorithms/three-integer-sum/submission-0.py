class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        indexes = set()
        def two_pointer(numbers, target):
            pairs = []
            index1 = 1
            index2 = len(numbers)
            while index1 < index2:
                if numbers[index1-1] + numbers[index2-1] > target:
                    index2 -= 1
                elif numbers[index1-1] + numbers[index2-1] < target:
                    index1+=1
                else:
                    pairs.append((numbers[index1-1], numbers[index2-1]))
                    index1 += 1
                    index2 -= 1
            return pairs

        for i in range(len(nums)):
            target = -nums[i]
            numsnew = nums[i+1:]
            for a,b in two_pointer(numsnew, target):
                indexes.add((nums[i], a, b))
        return [list(t) for t in indexes]
