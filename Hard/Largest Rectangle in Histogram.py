# Problem 84 - Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0
        
        for i, height in enumerate(heights):
            j = i

            while stack and stack[-1][1] > height:
                maxArea = max(maxArea, stack[-1][1] * (i - stack[-1][0]))
                j = stack[-1][0]
                stack.pop()
            
            stack.append([j, height])

        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))
        
        return maxArea