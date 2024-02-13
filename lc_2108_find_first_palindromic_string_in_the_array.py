class Solution:
    @staticmethod
    def first_palindrome(words: list[str]) -> str:
        try:
            return [word for word in words if word == word[::-1]][0]
        except IndexError:
            return ""


if __name__ == "__main__":
    assert (
        Solution().first_palindrome(words=["abc", "car", "ada", "racecar", "cool"])
        == "ada"
    )
    assert Solution().first_palindrome(words=["notapalindrome", "racecar"]) == "racecar"
    assert Solution().first_palindrome(words=["def", "ghi"]) == ""
