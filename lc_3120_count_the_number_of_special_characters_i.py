class Solution:
    @staticmethod
    def number_of_special_chars(word: str) -> int:
        lower_chars: list[bool] = [False for _ in range(26)]
        upper_chars: list[bool] = [False for _ in range(26)]

        for c in word:
            asc: int = ord(c)

            if c.islower():
                lower_chars[asc - 97] = True
            else:
                upper_chars[asc - 65] = True

        return len(
            [
                True
                for lower_char, upper_char in zip(lower_chars, upper_chars)
                if lower_char and upper_char
            ]
        )


if __name__ == "__main__":
    assert Solution.number_of_special_chars(word="aaAbcBC") == 3
    assert Solution.number_of_special_chars(word="abc") == 0
    assert Solution.number_of_special_chars(word="abBCab") == 1
