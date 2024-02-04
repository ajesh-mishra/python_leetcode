class Solution:
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()
        x, y, z = nums

        if x + y <= z:
            return "none"

        length = len(set(nums))

        if length == 1:
            return "equilateral"
        elif length == 2:
            return "isosceles"
        else:
            return "scalene"


if __name__ == "__main__":
    assert Solution().triangleType(nums=[3, 3, 3]) == "equilateral"
    assert Solution().triangleType(nums=[3, 4, 5]) == "scalene"
