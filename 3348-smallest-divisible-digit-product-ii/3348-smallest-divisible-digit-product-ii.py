class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        need = {2: 0, 3: 0, 5: 0, 7: 0}

        while t > 1:
            if t % 2 == 0:
                need[2] += 1
                t //= 2
            elif t % 3 == 0:
                need[3] += 1
                t //= 3
            elif t % 5 == 0:
                need[5] += 1
                t //= 5
            elif t % 7 == 0:
                need[7] += 1
                t //= 7
            else:
                return "-1"


        factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0)
        }

        def make_digits(a, b, c, d):

            digits = []

            
            digits += ['5'] * c
            digits += ['7'] * d

           
            while a >= 3:
                digits.append('8')
                a -= 3

            while b >= 2:
                digits.append('9')
                b -= 2

            
            if a == 1 and b == 1:
                digits.append('6')
                a = 0
                b = 0

            elif a == 2 and b == 1:
               
                digits.append('2')
                digits.append('6')
                a = 0
                b = 0

            else:
                if a == 1:
                    digits.append('2')

                elif a == 2:
                    digits.append('4')

                if b == 1:
                    digits.append('3')

            
            digits.sort()

            return ''.join(digits)


        def can_fill(missing, slots):

            s = make_digits(
                missing[2],
                missing[3],
                missing[5],
                missing[7]
            )

            return len(s) <= slots


        def build_suffix(missing, slots):

            s = make_digits(
                missing[2],
                missing[3],
                missing[5],
                missing[7]
            )

            extra = slots - len(s)

            return '1' * extra + s


      
        n = len(num)

        prefix = [
            {2: 0, 3: 0, 5: 0, 7: 0}
            for _ in range(n + 1)
        ]


        zero_prefix = [False] * (n + 1)

        for i in range(n):

            prefix[i + 1] = prefix[i].copy()

            digit = int(num[i])

            zero_prefix[i + 1] = (
                zero_prefix[i] or digit == 0
            )

            if digit != 0:

                f = factors[digit]

                prefix[i + 1][2] += f[0]
                prefix[i + 1][3] += f[1]
                prefix[i + 1][5] += f[2]
                prefix[i + 1][7] += f[3]


        have = prefix[n]

        if (
            not zero_prefix[n]
            and have[2] >= need[2]
            and have[3] >= need[3]
            and have[5] >= need[5]
            and have[7] >= need[7]
        ):
            return num

        for i in range(n - 1, -1, -1):

            if zero_prefix[i]:
                continue

            curr = int(num[i])

            for digit in range(max(1, curr + 1), 10):

                curr_have = {
                    2: prefix[i][2],
                    3: prefix[i][3],
                    5: prefix[i][5],
                    7: prefix[i][7]
                }

                f = factors[digit]

                curr_have[2] += f[0]
                curr_have[3] += f[1]
                curr_have[5] += f[2]
                curr_have[7] += f[3]


                missing = {
                    2: max(0, need[2] - curr_have[2]),
                    3: max(0, need[3] - curr_have[3]),
                    5: max(0, need[5] - curr_have[5]),
                    7: max(0, need[7] - curr_have[7])
                }


                slots = n - i - 1


                if can_fill(missing, slots):

                    suffix = build_suffix(
                        missing,
                        slots
                    )

                    return (
                        num[:i]
                        + str(digit)
                        + suffix
                    )



        missing = need.copy()

        required_digits = make_digits(
            missing[2],
            missing[3],
            missing[5],
            missing[7]
        )

        length = max(
            n + 1,
            len(required_digits)
        )

        return (
            '1' * (length - len(required_digits))
            + required_digits
        )