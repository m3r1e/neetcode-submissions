class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        row = -1
        for i in range(rows):
            if matrix[i][0] <= target and target <= matrix[i][-1]:
                row = i
        
        if row == -1:
            return False

        def binarySearch(nums, target):
            r = len(nums)-1
            l = 0
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        if binarySearch(matrix[row], target) != -1:
            return True
        else:
            return False
