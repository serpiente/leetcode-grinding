from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # taken from https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

        k = l = len(nums) - 1

        while k > 0 and nums[k] <= nums[k - 1]:
            k -= 1

        if k == 0:
            nums.reverse()
            return

        while nums[l] <= nums[k - 1]:
            l -= 1

        nums[l], nums[k - 1] = nums[k - 1], nums[l]

        nums[k:] = reversed(nums[k:])
