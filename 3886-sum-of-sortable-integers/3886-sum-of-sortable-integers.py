class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        target = sorted(nums)

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            arr = []
            valid = True

            for i in range(0, n, k):
                block = nums[i:i + k]
                breaks = []

                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        breaks.append(j)

                if len(breaks) > 1:
                    valid = False
                    break

                if len(breaks) == 1:
                    start = breaks[0] + 1
                    block = block[start:] + block[:start]

                arr.extend(block)

            if valid and arr == target:
                ans += k

        return ans