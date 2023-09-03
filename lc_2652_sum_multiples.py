class Solution:
    def sum_of_multiples(self, n: int) -> int:
        solutions = {
            "solution": self.solution,
            "solution_1": self.solution_1,
            "solution_2": self.solution_2,
        }
        return solutions["solution_2"](n)

    @staticmethod
    def solution(n: int) -> int:
        return sum(
            [
                num
                for num in range(n + 1)
                if num % 3 == 0 or num % 5 == 0 or num % 7 == 0
            ]
        )

    @staticmethod
    def solution_1(n: int) -> int:
        result = 0
        for num in range(n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                result += num

        return result

    @staticmethod
    def solution_2(n: int) -> int:
        return sum(
            list(
                filter(
                    lambda num: num % 3 == 0 or num % 5 == 0 or num % 7 == 0,
                    range(n + 1),
                )
            )
        )


if __name__ == "__main__":
    # print(Solution().sum_of_multiples(7))
    assert Solution().sum_of_multiples(7) == 21
    assert Solution().sum_of_multiples(10) == 40
    assert Solution().sum_of_multiples(9) == 30
