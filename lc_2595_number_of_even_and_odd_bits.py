class Solution:
    def even_odd_bit(self, n: int) -> list[int]:
        even, odd = 0, 0
        for index, digit in enumerate(f"{n:b}"[::-1]):
            if index % 2 == 0 and digit == "1":
                even += 1
                continue
            if digit == "1":
                odd += 1

        return [even, odd]


if __name__ == "__main__":
    # print(Solution().even_odd_bit(n=17))
    assert Solution().even_odd_bit(n=17) == [2, 0]
    assert Solution().even_odd_bit(n=2) == [0, 1]
