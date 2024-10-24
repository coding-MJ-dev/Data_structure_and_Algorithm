# 84. Largest Rectangle in Histogram


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights.append(0)
        for i, n in enumerate(heights):
            while stack and heights[stack[-1]] > n:
                popInd = stack.pop()
                val = heights[popInd]
                bottom = i - stack[-1] - 1 if stack else i
                ans = max(ans, val * bottom)
            stack.append(i)
        return ans
