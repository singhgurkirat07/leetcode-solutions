class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        n = len(stoneValue)

        # dp[left][right] =
        # maximum score obtainable from stoneValue[left:right+1]
        dp = [[0] * n for _ in range(n)]

        # mx is used to store the best transition values
        mx = [[0] * n for _ in range(n)]

        # Prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        for i in range(n):
            mx[i][i] = stoneValue[i]

        for right in range(1, n):

            mid = right
            right_sum = 0
            total = stoneValue[right]

            for left in range(right - 1, -1, -1):

                total += stoneValue[left]

                # Move mid towards the balance point
                while mid > left and right_sum + stoneValue[mid] <= total - (right_sum + stoneValue[mid]):
                    right_sum += stoneValue[mid]
                    mid -= 1

                # Equal sums
                if right_sum * 2 == total:
                    dp[left][right] = max(
                        dp[left][right],
                        mx[left][mid]
                    )

                # Left side is smaller
                if mid > left:
                    dp[left][right] = max(
                        dp[left][right],
                        mx[left][mid - 1]
                    )

                # Right side is smaller
                if mid < right:
                    dp[left][right] = max(
                        dp[left][right],
                        mx[right][mid + 1]
                    )

                # Update mx
                mx[left][right] = max(
                    mx[left][right - 1],
                    dp[left][right] + total
                )

                mx[right][left] = max(
                    mx[right][left + 1],
                    dp[left][right] + total
                )

        return dp[0][n - 1]