class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # stack to store indices
        max_area = 0
        heights.append(0)  # Sentinel to ensure all bars are processed
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # height of the bar
                width = i if not stack else i - stack[-1] - 1  # width of the rectangle
                max_area = max(max_area, h * width)
            stack.append(i)
        
        return max_area
            