class Solution:
    @staticmethod
    def time_required_to_buy(tickets: list[int], k: int) -> int:
        return sum(
            [
                min(n, tickets[k]) if index <= k else min(n, tickets[k] - 1)
                for index, n in enumerate(tickets)
            ]
        )


if __name__ == "__main__":
    assert Solution.time_required_to_buy(tickets=[2, 3, 2], k=2) == 6
    assert Solution.time_required_to_buy(tickets=[5, 1, 1, 1], k=0) == 8
