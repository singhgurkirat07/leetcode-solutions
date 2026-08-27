class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        def build_remaining():
            res = []
            for i in range(26):
                res.append(chr(i + ord('a')) * cnt[i])
            return ''.join(res)

        for i in range(n):
            x = ord(target[i]) - ord('a')

            # Try to keep the prefix equal to target
            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
                continue

            # Can't match target[i].
            # Try the smallest character greater than target[i].
            for j in range(x + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    return ''.join(ans) + chr(j + ord('a')) + build_remaining()

            # No greater character here.
            # We need to backtrack.
            break

        # Backtrack through the prefix we matched
        for i in range(len(ans) - 1, -1, -1):
            x = ord(ans[i]) - ord('a')

            # Return this character to the pool
            cnt[x] += 1
            ans.pop()

            # Find the smallest character greater than ans[i]
            for j in range(x + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    return ''.join(ans) + chr(j + ord('a')) + build_remaining()

        return ""