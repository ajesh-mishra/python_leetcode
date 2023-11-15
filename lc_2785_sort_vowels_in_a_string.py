class Solution:
    @staticmethod
    def sort_vowels(s: str) -> str:
        VOWELS = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        result, vowels = "", []

        for c in s:
            if c in VOWELS:
                vowels.append(c)
                result += "_"
            else:
                result += c

        vowels.sort()
        final_result, count = "", 0

        for r in result:
            if r == "_":
                final_result += vowels[count]
                count += 1
                continue
            final_result += r

        return final_result


if __name__ == "__main__":
    assert Solution().sort_vowels(s="lEetcOde") == "lEOtcede"
    assert Solution().sort_vowels(s="lYmpH") == "lYmpH"
