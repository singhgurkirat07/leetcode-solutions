class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        curr_lcm = lcm(curr_lcm, coins[i])

                        if curr_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                multiples = x // curr_lcm

                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low