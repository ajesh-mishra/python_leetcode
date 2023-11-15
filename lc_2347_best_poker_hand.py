class Solution:
    def get_map(elements: list[int]) -> dict[int, int]:
        map = {}

        for element in elements:
            try:
                map[element] += 1
            except KeyError:
                map[element] = 1

        return map

    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        rank_map = Solution.get_map(ranks)
        suit_map = Solution.get_map(suits)

        if len(suit_map) == 1 and suit_map[suits[0]] == 5:
            return "Flush"
        elif max(rank_map.values()) >= 3:
            return "Three of a Kind"
        elif max(rank_map.values()) >= 2:
            return "Pair"
        else:
            return "High Card"


if __name__ == "__main__":
    assert (
        Solution().bestHand(ranks=[13, 2, 3, 1, 9], suits=["a", "a", "a", "a", "a"])
        == "Flush"
    )
    assert (
        Solution().bestHand(ranks=[4, 4, 2, 4, 4], suits=["d", "a", "a", "b", "c"])
        == "Three of a Kind"
    )
    assert (
        Solution().bestHand(ranks=[10, 10, 2, 12, 9], suits=["a", "b", "c", "a", "d"])
        == "Pair"
    )
