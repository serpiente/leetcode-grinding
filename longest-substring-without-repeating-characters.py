class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        m = 0
        last_index = [-1] * 256

        for i, s in enumerate(s):
            ordinal = ord(s)
            m = max(m, last_index[ordinal] + 1)
            last_index[ordinal] = i
            longest = max(longest, i - m + 1)

        return longest