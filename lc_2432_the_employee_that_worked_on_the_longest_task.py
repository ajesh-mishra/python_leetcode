class Solution:
    def hardest_worker(self, n: int, logs: list[list[int]]) -> int:
        min_id, max_time, prev_time = n + 1, 0, 0
        for id, time in logs:
            time -= prev_time
            prev_time += time
            if max_time < time:
                max_time, min_id = time, id
            if max_time == time and min_id > id:
                min_id = id
        return min_id


if __name__ == "__main__":
    assert Solution().hardest_worker(n=10, logs=[[0, 3], [2, 5], [0, 9], [1, 15]]) == 1
    assert Solution().hardest_worker(n=26, logs=[[1, 1], [3, 7], [2, 12], [7, 17]]) == 3
    assert Solution().hardest_worker(n=2, logs=[[0, 10], [1, 20]]) == 0
