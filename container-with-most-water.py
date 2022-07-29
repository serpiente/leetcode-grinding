from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_volume = (j - i) * min(height[i], height[j])

        while i < j:
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

            volume = (j - i) * min(height[i], height[j])

            max_volume = max(max_volume, volume)
        return max_volume