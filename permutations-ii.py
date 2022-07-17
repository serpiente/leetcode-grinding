from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, permutation, res):
        if not nums:
            res.append(permutation)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Avoid duplicates
            #Choose element, skipping duplicates,  and build permutations with remaining elements
            self.dfs(nums[:i] + nums[i + 1:], [nums[i]] + permutation, res)
        return res
