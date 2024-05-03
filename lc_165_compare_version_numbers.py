from itertools import zip_longest

class Solution:
    @staticmethod
    def compare_version(version1: str, version2: str) -> int:
        for a, b in zip_longest(version1.split("."), version2.split("."), fillvalue="0"):
            if int(a) > int(b):
                return 1
            if int(a) < int(b):
                return -1

        return 0


if __name__ == "__main__":
    assert Solution.compare_version(version1="1.01", version2="1.001") == 0
    assert Solution.compare_version(version1="1.0", version2="1.0.0") == 0
    assert Solution.compare_version(version1="0.1", version2="1.1") == -1
