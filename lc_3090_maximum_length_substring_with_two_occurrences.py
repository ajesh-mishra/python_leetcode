class Solution:
    @staticmethod
    def maximum_length_substring(s: str) -> int:
        char_set: set[str] = {c for c in s}
        map: dict[str, int] = {c: 0 for c in char_set}
        result: int = 0

        for c in s:
            if map[c] < 2:
                map[c] += 1
                continue

            result = max(result, sum(map.values()))
            map = {c: 0 for c in char_set}
            map[c] += 1

        result = max(result, sum(map.values()))
        return result


if __name__ == "__main__":
    print(Solution.maximum_length_substring(s="bcbbbcba"))
    # assert Solution.maximum_length_substring(s="bcbbbcba") == 4
    assert Solution.maximum_length_substring(s="aaaa") == 2
