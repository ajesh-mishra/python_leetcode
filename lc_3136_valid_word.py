class Solution:
    @staticmethod
    def is_valid(word: str) -> bool:
        if len(word) < 3:
            return False

        if not word.isalnum():
            return False

        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"

        has_vowels: bool = False
        has_consonants: bool = False

        for c in word:
            c = c.lower()
            if c in vowels:
                has_vowels = True
            if c in consonants:
                has_consonants = True
            if has_vowels and has_consonants:
                return True

        return False


if __name__ == "__main__":
    assert Solution.is_valid(word="234Adas")
    assert not Solution.is_valid(word="b3")
    assert not Solution.is_valid(word="a3$e")
