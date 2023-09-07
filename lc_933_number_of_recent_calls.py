class RecentCounter:
    window = 3000

    def __init__(self):
        self.count = []

    def ping(self, t: int) -> int:
        self.count.append(t)

        for index, time in enumerate(self.count[::-1]):
            if time < t - RecentCounter.window:
                return index

        return len(self.count)


if __name__ == "__main__":
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3
