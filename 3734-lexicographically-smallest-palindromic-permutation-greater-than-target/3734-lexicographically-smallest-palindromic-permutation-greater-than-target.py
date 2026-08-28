class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        # Check if palindrome is possible
        odd = [i for i in range(26) if freq[i] % 2]

        if len(odd) > 1:
            return ""

        mid = chr(97 + odd[0]) if odd else ""

        # Characters needed in left half
        half = [x // 2 for x in freq]
        m = n // 2

        def make_pal(left):
            return left + mid + left[::-1]

        # First check if target's left half itself can be used.
        # If its palindrome is > target, it is the smallest answer.
        cnt = half[:]
        left = []
        possible = True

        for i in range(m):
            c = ord(target[i]) - 97

            if cnt[c] == 0:
                possible = False
                break

            cnt[c] -= 1
            left.append(target[i])

        if possible:
            ans = make_pal(''.join(left))
            if ans > target:
                return ans

        # Otherwise find the smallest left half greater than
        # target's left half.
        for pos in range(m - 1, -1, -1):
            cnt = half[:]
            prefix = []
            possible = True

            # Match target before pos
            for i in range(pos):
                c = ord(target[i]) - 97

                if cnt[c] == 0:
                    possible = False
                    break

                cnt[c] -= 1
                prefix.append(target[i])

            if not possible:
                continue

            # Choose the smallest available character
            # greater than target[pos].
            cur = ord(target[pos]) - 97

            for c in range(cur + 1, 26):
                if cnt[c] == 0:
                    continue

                cnt[c] -= 1

                left = ''.join(prefix) + chr(97 + c)

                # Fill remaining characters in sorted order
                for x in range(26):
                    left += chr(97 + x) * cnt[x]

                return make_pal(left)

        return ""