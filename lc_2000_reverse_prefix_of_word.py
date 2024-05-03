class Solution:
    @staticmethod
    def reverse_prefix(word: str, ch: str) -> str:
        pos = word.find(ch)
        return word[:pos + 1][::-1] + word[pos + 1:]


if __name__ == "__main__":
    assert Solution.reverse_prefix(word="abcdefd", ch="d") == "dcbaefd"
    assert Solution.reverse_prefix(word="xyxzxe", ch="z") == "zxyxxe"
    assert Solution.reverse_prefix(word="abcd", ch="z") == "abcd"
