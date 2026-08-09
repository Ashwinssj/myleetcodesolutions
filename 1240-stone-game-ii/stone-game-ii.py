class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        dp = {}

        def solve(i, m):
            if i >= n:
                return 0

            if (i, m) in dp:
                return dp[(i, m)]

            best = 0

            for X in range(1, 2 * m + 1):
                if i + X > n:
                    break

                opponent = solve(i + X, max(m, X))

                current = suffix[i] - opponent

                best = max(best, current)

            dp[(i, m)] = best
            return best

        return solve(0, 1)