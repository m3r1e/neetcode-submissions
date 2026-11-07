class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index1 = 0
        index2 = len(heights)-1
        maxArea = 0
        while index1 < index2:
            currArea = (index2 - index1) * min(heights[index1], heights[index2])
            if currArea > maxArea:
                maxArea = currArea
            if heights[index1] < heights[index2]:
                index1 += 1
            elif heights[index1] > heights[index2]:
                index2 -= 1
            else:
                index1 += 1
        
        return maxArea