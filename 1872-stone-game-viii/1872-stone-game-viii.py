class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + stones[i - 1]

        best = prefix[n]

        for i in range(n - 1, 1, -1):
            best = max(best, prefix[i] - best)

        return best