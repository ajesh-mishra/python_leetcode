class Solution:
    @staticmethod
    def find_even_numbers(digits: list[int]) -> list[int]:
        from itertools import permutations

        return sorted(
            filter(
                lambda x: x > 99 and x % 2 == 0,
                [
                    t[0] * 100 + t[1] * 10 + t[2]
                    for t in list(set(permutations(digits, 3)))
                ],
            )
        )

    def find_even_numbers_1(self, digits: list[int]) -> list[int]:
        result: list[int] = []
        first_digits = [digit for digit in digits if digit != 0]
        last_digits = [digit for digit in digits if digit % 2 == 0]

        def get_next_digits(num, is_last: bool = True) -> set[int]:
            if is_last:
                tmp: list[int] = last_digits[:]
            else:
                tmp: list[int] = digits[:]

            for x in str(num):
                try:
                    tmp.remove(int(x))
                except ValueError:
                    pass

            return set(tmp)

        def inner(num: int) -> None:
            length = len(str(num))

            if length == 3:
                if num not in result:
                    result.append(num)
                return None

            if length == 2:
                for d in get_next_digits(num=num):
                    inner(num * 10 + d)
                return None

            for d in get_next_digits(num=num, is_last=False):
                inner(num * 10 + d)

        for d in first_digits:
            inner(num=d)

        return sorted(result)


if __name__ == "__main__":
    assert Solution().find_even_numbers(digits=[2, 1, 3, 0]) == [
        102,
        120,
        130,
        132,
        210,
        230,
        302,
        310,
        312,
        320,
    ]
    assert Solution().find_even_numbers(digits=[2, 2, 8, 8, 2]) == [
        222,
        228,
        282,
        288,
        822,
        828,
        882,
    ]
    assert Solution().find_even_numbers(digits=[3, 7, 5]) == []
