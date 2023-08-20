class Solution:
    @staticmethod
    def split_words_by_separator(words: list[str], separator: str) -> list[str]:
        result = []
        for word in words:
            result = [*result, *[w for w in word.split(separator) if len(w) > 0]]

        return result


if __name__ == '__main__':
    print(Solution().split_words_by_separator(words=["one.two.three", "four.five", "six"], separator="."))
    print(Solution().split_words_by_separator(words=["$easy$", "$problem$"], separator="$"))
    print(Solution().split_words_by_separator(words=["|||"], separator="|"))
