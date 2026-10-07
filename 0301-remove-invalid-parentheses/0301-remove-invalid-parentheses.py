from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def isValid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        ans = []

        found = False

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                # Check if current string is valid
                if isValid(curr):
                    ans.append(curr)
                    found = True

                # Don't generate next level
                # once we found valid strings
                if found:
                    continue

                # Remove one parenthesis
                for i in range(len(curr)):

                    if curr[i] != '(' and curr[i] != ')':
                        continue

                    next_string = curr[:i] + curr[i + 1:]

                    if next_string not in visited:
                        visited.add(next_string)
                        queue.append(next_string)

            # First valid level = minimum removals
            if found:
                break

        return ans