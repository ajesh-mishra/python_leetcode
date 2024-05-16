class Solution:
    @staticmethod
    def find_permutation_difference(s: str, t: str) -> int:
        char_map: list[int] = [0 for _ in range(26)]

        for index, (sc, tc) in enumerate(zip(s, t)):
            pos = ord(sc) - 97
            char_map[pos] = abs(char_map[pos] - index)

            pos = ord(tc) - 97
            char_map[pos] = abs(char_map[pos] - index)

        return sum(char_map)


if __name__ == "__main__":
    assert Solution.find_permutation_difference(s="abc", t="bac") == 2
    assert Solution.find_permutation_difference(s="abcde", t="edbac") == 12
