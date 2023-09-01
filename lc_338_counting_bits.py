class Solution:
    @staticmethod
    def count_bits(n: int) -> list[int]:
        return [f'{i:b}'.count('1') for i in range(0, n + 1)]


if __name__ == '__main__':
    print(Solution().count_bits(2))
