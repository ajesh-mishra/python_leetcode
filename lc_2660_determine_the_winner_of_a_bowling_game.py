class Solution:
    @staticmethod
    def calculate_total(player: list[int]) -> int:
        total, last_ten = 0, -100
        for index, score in enumerate(player):
            if index - last_ten <= 2:
                total += score * 2
            else:
                total += score

            if score == 10:
                last_ten = index

        return total

    def is_winner(self, player1: list[int], player2: list[int]) -> int:
        if self.calculate_total(player1) == self.calculate_total(player2):
            return 0
        elif self.calculate_total(player1) > self.calculate_total(player2):
            return 1
        else:
            return 2


if __name__ == "__main__":
    print(Solution().is_winner(player1=[4, 10, 7, 9], player2=[6, 5, 2, 3]))
    print(Solution().is_winner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]))
    print(Solution().is_winner(player1=[2, 3], player2=[4, 1]))
