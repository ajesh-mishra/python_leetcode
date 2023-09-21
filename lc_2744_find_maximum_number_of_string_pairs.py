class Solution:
    @staticmethod
    def maximum_number_of_string_pairs(words: list[str]) -> int:
        count = 0
        words_reversed = [word[::-1] for word in words]
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] == words_reversed[j]:
                    count += 1
        return count


if __name__ == "__main__":
    assert (
        Solution().maximum_number_of_string_pairs(["cd", "ac", "dc", "ca", "zz"]) == 2
    )
    assert Solution().maximum_number_of_string_pairs(["ab", "ba", "cc"]) == 1
