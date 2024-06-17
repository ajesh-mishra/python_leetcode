class Solution:
    @staticmethod
    def count_complete_day_pairs(hours: list[int]) -> int:
        return len(
            [
                True
                for i in range(len(hours) - 1)
                for j in range(i + 1, len(hours))
                if (hours[i] + hours[j]) % 24 == 0
            ]
        )


if __name__ == "__main__":
    assert Solution.count_complete_day_pairs(hours=[12, 12, 30, 24, 24]) == 2
    assert Solution.count_complete_day_pairs(hours=[72, 48, 24, 3]) == 3
