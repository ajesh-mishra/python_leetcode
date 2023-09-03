class Solution:
    @staticmethod
    def find_delayed_arrival_time(arrival_time: int, delayed_time: int) -> int:
        return (arrival_time + delayed_time) % 24


if __name__ == "__main__":
    assert Solution().find_delayed_arrival_time(15, 5) == 20
    assert Solution().find_delayed_arrival_time(13, 11) == 0
