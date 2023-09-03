class Solution(object):
    @staticmethod
    def count_seniors(details: list[str]):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                count += 1

        return count


if __name__ == "__main__":
    assert (
        Solution().count_seniors(
            ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
        )
        == 2
    )
    assert Solution().count_seniors(["1313579440F2036", "2921522980M5644"]) == 0
