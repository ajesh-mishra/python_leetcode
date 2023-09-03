class Solution:
    @staticmethod
    def is_acronym(words: list[str], s: str) -> bool:
        return "".join([word[0] for word in words]) == s


if __name__ == "__main__":
    assert Solution.is_acronym(words=["alice", "bob", "charlie"], s="abc")
    assert Solution.is_acronym(
        words=["never", "gonna", "give", "up", "on", "you"], s="ngguoy"
    )
    assert not Solution.is_acronym(words=["an", "apple"], s="a")
