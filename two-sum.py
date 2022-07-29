from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {n: i for i, n in enumerate(nums)}

        for i, n in enumerate(nums):
            remainer = target - n
            if remainer in pos and pos[remainer] != i:
                return [i, pos[remainer]]
