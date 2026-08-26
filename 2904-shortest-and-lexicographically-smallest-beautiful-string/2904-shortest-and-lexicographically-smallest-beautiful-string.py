class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have exactly k ones
            if ones == k:
                # Remove unnecessary leading zeros
                while left <= right and s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                # Update answer
                if (best == "" or
                    len(curr) < len(best) or
                    (len(curr) == len(best) and curr < best)):
                    best = curr

                # Move left past the first 1
                if s[left] == '1':
                    ones -= 1
                    left += 1

        return best