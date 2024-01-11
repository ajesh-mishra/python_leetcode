class Solution:
    def splitNum(self, num: int) -> int:
        num_list = [digit for digit in str(num)]
        num_list.sort()

        even_digits = [digit for index, digit in enumerate(num_list) if index % 2 == 0]
        odd_digits = [digit for index, digit in enumerate(num_list) if index % 2 != 0]

        return int("".join(even_digits)) + int("".join(odd_digits))


if __name__ == "__main__":
    assert Solution().splitNum(num=4325) == 59
    assert Solution().splitNum(num=687) == 75
