class Solution:
    @staticmethod
    def max_length_between_equal_characters(s: str) -> int:
        char_map = [[] for _ in range(26)]
        result = -1

        for index, c in enumerate(s):
            char_map[ord(c) - 97].append(index)

        for positions in char_map:
            if len(positions) < 2:
                continue
            result = max(result, positions[-1] - positions[0] - 1)

        return -1 if result == -1 else result


if __name__ == "__main__":
    assert Solution().max_length_between_equal_characters(s="aa") == 0
    assert Solution().max_length_between_equal_characters(s="abca") == 2
    assert Solution().max_length_between_equal_characters(s="cbzxy") == -1
