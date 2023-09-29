class Solution:
    def maximum_odd_binary_number(self, s: str) -> str:
        length: int = len(s)
        ones: int = len([1 for x in s if x == "1"])
        result_1: str = "1" * (ones - 1)
        result_2: str = "0" * (length - ones)
        print(f"{result_1}{result_2}1")
        return f"{result_1}{result_2}1"


if __name__ == "__main__":
    assert Solution().maximum_odd_binary_number("010") == "001"
    assert Solution().maximum_odd_binary_number("0101") == "1001"
