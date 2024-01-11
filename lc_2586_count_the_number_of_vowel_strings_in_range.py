class Solution:
    def vowel_strings(self, words: list[str], left: int, right: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        return len(
            [
                word
                for word in words[left : right + 1]
                if word[0] in vowels and word[-1] in vowels
            ]
        )


if __name__ == "__main__":
    assert Solution().vowel_strings(words=["are", "amy", "u"], left=0, right=2) == 2
    assert (
        Solution().vowel_strings(
            words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4
        )
        == 3
    )
