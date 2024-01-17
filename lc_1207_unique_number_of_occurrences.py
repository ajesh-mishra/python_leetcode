class Solution:
    def unique_occurrences(self, arr: list[int]) -> bool:
        map_arr = {}

        for num in arr:
            if num in map_arr:
                map_arr[num] += 1
            else:
                map_arr[num] = 1

        return len(map_arr.values()) == len(set(map_arr.values()))


if __name__ == '__main__':
    assert Solution().unique_occurrences(arr = [1, 2, 2, 1, 1, 3])
    assert Solution().unique_occurrences(arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
    assert not Solution().unique_occurrences(arr = [1, 2])