class Solution:
    def remove_trailing_zeros(self, num: str) -> str:
        end = len(num)
        while num[0:end].endswith("0"):
            end -= 1

        return num[0:end]


if __name__ == "__main__":
    # print(Solution().remove_trailing_zeros(num="51230100"))
    assert Solution().remove_trailing_zeros(num="51230100") == "512301"
    assert Solution().remove_trailing_zeros(num="123") == "123"
