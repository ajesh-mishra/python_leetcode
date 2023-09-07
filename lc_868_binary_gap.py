class Solution:
    def binary_gap(self, n: int) -> int:
        result, prev = 0, None
        for index, char in enumerate(f"{n:b}"):
            if char == "1":
                if prev is not None:
                    result = max(result, index - prev)
                prev = index

        return result


if __name__ == "__main__":
    assert Solution().binary_gap(22) == 2
    assert Solution().binary_gap(8) == 0
    assert Solution().binary_gap(5) == 2
