class Solution:
    @staticmethod
    def find_peaks(mountain: list[int]) -> list[int]:
        return [
            i + 1
            for i in range(len(mountain) - 2)
            if mountain[i] < mountain[i + 1] > mountain[i + 2]
        ]


if __name__ == "__main__":
    assert Solution().find_peaks(mountain=[2, 4, 4]) == []
    assert Solution().find_peaks(mountain=[1, 4, 3, 8, 5]) == [1, 3]
