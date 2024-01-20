class Solution:
    @staticmethod
    def is_power_of_three(n: int) -> bool:
        def inner(num: int, rem: int) -> bool:
            if rem != 0:
                return False
            if num < 1:
                return False
            if num == 1:
                return True

            return inner(num // 3, num % 3)

        return inner(n, 0)


if __name__ == "__main__":
    assert Solution().is_power_of_three(n=27)
    assert Solution().is_power_of_three(n=1)
    assert not Solution().is_power_of_three(n=45)
    assert not Solution().is_power_of_three(n=0)
    assert not Solution().is_power_of_three(n=-1)
