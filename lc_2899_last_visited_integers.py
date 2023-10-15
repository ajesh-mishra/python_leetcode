class Solution:
    def lastVisitedIntegers(self, words: list[str]) -> list[int]:
        stack: list[int] = []
        result: list[int] = []
        last_int: int | None = None

        for index, word in enumerate(words):
            if word == "prev":
                if last_int is None:
                    pos = -1
                else:
                    pos = last_int - index
                try:
                    result.append(stack[pos])
                except IndexError:
                    result.append(-1)
            else:
                last_int = index
                stack.append(int(word))

        return result


if __name__ == "__main__":
    assert Solution().lastVisitedIntegers(words=["1", "2", "prev", "prev", "prev"]) == [
        2,
        1,
        -1,
    ]
    assert Solution().lastVisitedIntegers(words=["1", "prev", "2", "prev", "prev"]) == [
        1,
        2,
        1,
    ]
