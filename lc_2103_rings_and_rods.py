class Solution:
    @staticmethod
    def count_points(rings: str) -> int:
        ring_map: dict[int, set[str]] = {}

        for i in range(0, len(rings), 2):
            ring_type, rod = rings[i], int(rings[i + 1])
            if rod not in ring_map:
                ring_map[rod] = set()
            ring_map[rod].add(ring_type)

        return len(["x" for r in ring_map.values() if len(r) == 3])


if __name__ == "__main__":
    assert Solution().count_points("B9R9G0R4G6R8R2R9G9") == 1
    assert Solution().count_points("B0B6G0R6R0R6G9") == 1
    assert Solution().count_points("B0R0G0R9R0B0G0") == 1
    assert Solution().count_points("G4") == 0
