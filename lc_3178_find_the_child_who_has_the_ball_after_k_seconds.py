class Solution:
    @staticmethod
    def number_of_child(n: int, k: int) -> int:
        n -= 1

        if n > k:
            return k

        oscillations: int = k // n
        reminder: int = k % n

        if oscillations % 2 == 0:
            return reminder

        return n - reminder


if __name__ == "__main__":
    assert Solution.number_of_child(n=3, k=5) == 1
    assert Solution.number_of_child(n=5, k=6) == 2
    assert Solution.number_of_child(n=4, k=2) == 2
