from typing import Any, Generator


class Solution:
    @staticmethod
    def is_subsequence(s: str, t: str) -> bool:
        s_chars: Generator[str, Any, None] = (c for c in s)
        t_chars: Generator[str, Any, None] = (c for c in t)
        result: str = ""
        while (sc := next(s_chars, None)) is not None:
            while (tc := next(t_chars, None)) is not None:
                if sc == tc:
                    result += sc
                    break

        return s == result


if __name__ == "__main__":
    assert Solution().is_subsequence(s="abc", t="ahbgdc")
    assert not Solution().is_subsequence(s="axc", t="ahbgdc")
