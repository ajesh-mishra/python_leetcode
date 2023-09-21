class Solution:
    @staticmethod
    def gcd(a: int, b: int) -> int:
        result = min(a, b)
        while result > 0:
            if a % result == 0 and b % result == 0:
                break
            result -= 1
        return result

    @staticmethod
    def count_beautiful_pairs(nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            first_digit = int(str(nums[i])[0])
            for j in range(i + 1, len(nums)):
                last_digit = nums[j] % 10
                if Solution.gcd(first_digit, last_digit) == 1:
                    count += 1
        return count


if __name__ == "__main__":
    assert Solution().count_beautiful_pairs(nums=[2, 5, 1, 4]) == 5
    assert Solution().count_beautiful_pairs(nums=[11, 21, 12]) == 2
