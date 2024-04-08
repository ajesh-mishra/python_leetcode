def merge_sort(nums: list[int]) -> list[int]:
    def merge(a: list[int], b: list[int]) -> list[int]:
        result, i, j = [], 0, 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        if i < len(a):
            result.extend(a[i:])
        if j < len(b):
            result.extend(b[j:])

        return result

    def inner(n: list[int]) -> list[int]:
        if len(n) == 1:
            return n

        mid = len(n) // 2
        return merge(inner(n[:mid]), inner(n[mid:]))

    return inner(nums)


if __name__ == "__main__":
    assert merge_sort([1, 4, 9, 2, 6, 7]) == [1, 2, 4, 6, 7, 9]
    assert merge_sort([1, 4, 9, 2, 6, 7, 3, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort([1, 292, 5, 11, 93298, 63, 9, 99, 765]) == [
        1,
        5,
        9,
        11,
        63,
        99,
        292,
        765,
        93298,
    ]
