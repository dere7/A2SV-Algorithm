class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start, end = 0, n - 1
        max_area = 0
        while start < end:
            base = end - start
            if height[start] <= height[end]:
                h = height[start]
                start += 1
            else:
                h = height[end]
                end -= 1
            if base * h > max_area:
                max_area = base * h
        return max_area
