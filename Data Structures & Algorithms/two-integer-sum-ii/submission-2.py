class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 1
        index2 = len(numbers)
        while True:
            if numbers[index1-1] + numbers[index2-1] > target:
                index2 -= 1
            elif numbers[index1-1] + numbers[index2-1] < target:
                index1+=1
            else:
                return [index1, index2]
        

