class Solution:
    @staticmethod
    def is_ugly(n: int) -> bool:
        if n < 1:
            return False

        for prime in (2, 3, 5):
            while n % prime == 0:
                n /= prime

        return n == 1


if __name__ == '__main__':
    assert Solution().is_ugly(6)
    assert Solution().is_ugly(1)
    assert not Solution().is_ugly(14)
