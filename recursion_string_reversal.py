def string_reversal(string: str) -> str:
    s = iter(string)

    def inner() -> str:
        try:
            n = next(s)
        except StopIteration:
            return ""

        return inner() + n

    return inner()


if __name__ == "__main__":
    assert string_reversal("ajesh mishra") == "arhsim hseja"
