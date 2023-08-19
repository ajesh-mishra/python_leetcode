class Solution:
    @staticmethod
    def circular_game_losers(n: int, k: int) -> list[int]:
        scores = [0 for _ in range(n + 1)]
        scores[0], scores[1] = 1, 1
        rounds, player = 1, 1

        while scores[player] <= 1:
            pos = player + (rounds * k) % n
            if pos > n:
                player = pos - n
            else:
                player = pos

            scores[player] += 1
            rounds += 1

        return [index for index, score in enumerate(scores) if score == 0]


if __name__ == '__main__':
    assert Solution().circular_game_losers(5, 2) == [4,5]
    assert Solution().circular_game_losers(4, 4) == [2,3,4]
