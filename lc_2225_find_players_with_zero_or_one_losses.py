class Solution:
    @staticmethod
    def find_winners(matches: list[list[int]]) -> list[list[int]]:
        winners = set([w[0] for w in matches])
        losers = {}

        for l in matches:
            if l[1] in losers:
                losers[l[1]] += 1
            else:
                losers[l[1]] = 1

        lost_one_match = [player for player, count in losers.items() if count == 1]
        players_never_lost = list(winners.difference(losers.keys()))

        return [sorted(players_never_lost), sorted(lost_one_match)]


if __name__ == "__main__":
    assert Solution().find_winners(
        [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    ) == [[1, 2, 10], [4, 5, 7, 8]]
    assert Solution().find_winners([[2, 3], [1, 3], [5, 4], [6, 4]]) == [
        [1, 2, 5, 6],
        [],
    ]
