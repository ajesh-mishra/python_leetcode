# 2670. Find the Distinct Difference Array

You are given a 0-indexed array `nums` of length `n`.

The distinct difference array of `nums` is an array `diff` of length n such that `diff[i]` is equal to the number of distinct elements in the suffix `nums[i + 1, ..., n - 1]` subtracted from the number of distinct elements in the prefix `nums[0, ..., i]`.

Return the distinct difference array of `nums`.

Note that `nums[i, ..., j]` denotes the subarray of nums starting at index `i` and ending at index `j` inclusive. Particularly, if `i > j` then `nums[i, ..., j]` denotes an empty subarray.

```python
class Solution:
    def distinct_difference_array(self, nums: list[int]) -> list[int]:
        pass
```

```bash
python solution.py
```

## Constraints

1. `1 <= n == nums.length <= 50`
2. `1 <= nums[i] <= 50`