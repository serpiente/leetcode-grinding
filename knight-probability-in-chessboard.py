class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[-1] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(x, y, remaining_moves):
            if x < 0 or x >= n or y < 0 or y >= n:
                return 0

            if remaining_moves == 0:
                return 1

            if dp[x][y][remaining_moves] != -1:
                return dp[x][y][remaining_moves]

            offsets = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]

            inside_count = 0
            for dx, dy in offsets:
                inside_count += solve(x + dx, y + dy, remaining_moves - 1)
            dp[x][y][remaining_moves] = inside_count
            return inside_count

        return solve(row, column, k) / 8 ** k


from functools import cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def solve(x, y, remaining_moves):
            if x < 0 or x >= n or y < 0 or y >= n:
                return 0

            if remaining_moves == 0:
                return 1

            offsets = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]

            inside_count = 0
            for dx, dy in offsets:
                inside_count += solve(x + dx, y + dy, remaining_moves - 1)
            return inside_count

        return solve(row, column, k) / 8 ** k


