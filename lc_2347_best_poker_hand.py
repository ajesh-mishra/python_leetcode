class Solution:
    @staticmethod
    def get_map(elements: list[int | str]) -> dict[int | str, int]:
        my_map: dict[int | str, int] = {}

        for element in elements:
            try:
                my_map[element] += 1
            except KeyError:
                my_map[element] = 1

        return my_map

    def best_hand(self, ranks: list[int], suits: list[str]) -> str:
        rank_map = self.get_map(ranks)
        suit_map = self.get_map(suits)

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
        Solution().best_hand(ranks=[13, 2, 3, 1, 9], suits=["a", "a", "a", "a", "a"])
        == "Flush"
    )
    assert (
        Solution().best_hand(ranks=[4, 4, 2, 4, 4], suits=["d", "a", "a", "b", "c"])
        == "Three of a Kind"
    )
    assert (
        Solution().best_hand(ranks=[10, 10, 2, 12, 9], suits=["a", "b", "c", "a", "d"])
        == "Pair"
    )
