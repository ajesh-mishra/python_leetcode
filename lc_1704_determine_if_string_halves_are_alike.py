class Solution:
    def halves_are_alike(self, s: str) -> bool:
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        return len(
            [
                char
                for index, char in enumerate(s)
                if char in vowels and index < len(s) // 2
            ]
        ) == len(
            [
                char
                for index, char in enumerate(s)
                if char in vowels and index >= len(s) // 2
            ]
        )


if __name__ == "__main__":
    assert Solution().halves_are_alike(s="book")
    assert not Solution().halves_are_alike(s="textbook")
