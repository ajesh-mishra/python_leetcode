from collections import defaultdict
from typing import DefaultDict


class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> int:
        char_map: DefaultDict[str, int] = defaultdict(int)
        result: int = 0
        has_odd: bool = False

        for c in s:
            char_map[c] += 1

        for _, count in char_map.items():
            if count == 1:
                has_odd = True
            elif count % 2 == 1:
                result += count - 1
                has_odd = True
            else:
                result += count

        return result + 1 if has_odd else result


if __name__ == "__main__":
    assert Solution.longest_palindrome(s="abccccdd") == 7
    assert Solution.longest_palindrome(s="a") == 1
    assert Solution.longest_palindrome(s="bb") == 2
