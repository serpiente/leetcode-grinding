class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1] * (maxMove + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        def solve(i, j, moves):
            if moves < 0:
                return 0

            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            if dp[i][j][moves] != -1:
                return dp[i][j][moves]

            cell_moves = solve(i - 1, j, moves - 1) + \
                         solve(i + 1, j, moves - 1) + \
                         solve(i, j - 1, moves - 1) + \
                         solve(i, j + 1, moves - 1)

            dp[i][j][moves] = cell_moves

            return cell_moves % 1000000007

        return solve(startRow, startColumn, maxMove)

