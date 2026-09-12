class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0                               # left 
        r = len(heights) - 1                # right
        maxi = 0
        w = len(heights) - 1                # width
        while l != r:
            h = min(heights[l], heights[r]) # height
            maxi = max(maxi, h * w)
            w -= 1
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1

        return maxi