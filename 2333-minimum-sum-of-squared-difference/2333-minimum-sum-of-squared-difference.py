class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int
    ) -> int:

        diff = [
            abs(nums1[i] - nums2[i])
            for i in range(len(nums1))
        ]

        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        # Find the minimum feasible target level
        while left < right:
            mid = (left + right) // 2

            operations = sum(
                max(0, d - mid) for d in diff
            )

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left

        # Reduce all differences above the target level
        operations = 0
        ans = 0

        for d in diff:
            if d > level:
                operations += d - level
                ans += level * level
            else:
                ans += d * d

        # Spend the remaining operations
        remaining = k - operations
        ans -= remaining * (2 * level - 1)

        return ans