class Solution:
    @staticmethod
    def clear_digits(s: str) -> str:
        def inner(_s: str) -> str:
            pos: int | None = None

            for index, c in enumerate(_s):
                if c.isdigit():
                    pos = index
                    break

            if pos is None:
                return _s
            elif pos <= 1:
                return inner(_s[pos + 1 :])
            else:
                return inner(_s[: pos - 1] + _s[pos + 1 :])

        return inner(s)


if __name__ == "__main__":
    assert Solution.clear_digits(s="abc") == "abc"
    assert Solution.clear_digits(s="cb34") == ""
    # assert Solution.clearDigits() == ""
