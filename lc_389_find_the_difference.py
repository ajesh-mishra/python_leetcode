class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        map = [0 for _ in range(26)]

        for c in s:
            map[ord(c) - 97] += 1

        for c in t:
            map[ord(c) - 97] -= 1
            if map[ord(c) - 97] == -1:
                return c


if __name__ == "__main__":
    assert Solution().find_the_difference(s="abcd", t="abcde") == "e"
    assert Solution().find_the_difference(s="", t="y") == "y"
