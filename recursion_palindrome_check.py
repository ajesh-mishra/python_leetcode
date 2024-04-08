def is_palindrome(s: str) -> bool:
    def inner(start: int, end: int) -> bool:
        if start >= end:
            return True
        if s[start] != s[end]:
            return False

        return inner(start + 1, end - 1)

    return inner(0, len(s) - 1)


if __name__ == "__main__":
    assert is_palindrome("kayak")
    assert is_palindrome("kayyak")
    assert not is_palindrome("kayakd")
