from collections import defaultdict


class Solution:
    @staticmethod
    def frequency_sort(s: str) -> str:
        char_map: dict[str, int] = defaultdict(int)

        for c in s:
            char_map[c] += 1

        char_map_tmp: list[tuple[str, int]] = [
            (char, count) for char, count in char_map.items()
        ]

        sorted_map: list[tuple[str, int]] = sorted(
            char_map_tmp, key=lambda x: x[1], reverse=True
        )

        return "".join([char * count for char, count in sorted_map])
