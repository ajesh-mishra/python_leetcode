class Solution:
    @staticmethod
    def find_minimum_operations(s1: str, s2: str, s3: str) -> int:
        common: int = 0

        for i in range(max(len(s1), len(s2), len(s3))):
            try:
                if s1[i] == s2[i] == s3[i]:
                    continue
                elif i == 0:
                    return -1
                else:
                    raise IndexError
            except IndexError:
                common = i
                break

        if common == 0:
            return 0

        return len(s1) + len(s2) + len(s3) - (3 * common)


if __name__ == "__main__":
    # print(Solution().find_minimum_operations(s1="a", s2="a", s3="a"))
    assert Solution().find_minimum_operations(s1="abc", s2="abb", s3="ab") == 2
    assert Solution().find_minimum_operations(s1="dac", s2="bac", s3="cac") == -1
    assert Solution().find_minimum_operations(s1="a", s2="a", s3="a") == 0
    assert Solution().find_minimum_operations(s1="a", s2="aabc", s3="a") == 3
