class Solution:
    @staticmethod
    def find_k_distant_indices(nums: list[int], key: int, k: int) -> list[int]:
        indices: list[int] = [index for index, num in enumerate(nums) if num == key]
        k_distant_indices: set[int] = set()

        for index in indices:
            k_distant_indices.update(
                {i for i in range(index - k, index + k + 1) if 0 <= i < len(nums)}
            )

        return sorted(list(k_distant_indices))


if __name__ == "__main__":
    assert Solution.find_k_distant_indices(nums=[3, 4, 9, 1, 3, 9, 5], key=9, k=1) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
    assert Solution.find_k_distant_indices(nums=[2, 2, 2, 2, 2], key=2, k=2) == [
        0,
        1,
        2,
        3,
        4,
    ]
