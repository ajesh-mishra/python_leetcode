class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x_is_even = (ord(coordinates[0]) - 96) % 2 == 0
        y_is_even = (int(coordinates[1])) % 2 == 0

        return x_is_even ^ y_is_even


if __name__ == "__main__":
    assert Solution().squareIsWhite(coordinates="h3")
    assert not Solution().squareIsWhite(coordinates="a1")
    assert not Solution().squareIsWhite(coordinates="c7")
