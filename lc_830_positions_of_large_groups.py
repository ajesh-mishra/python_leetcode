class Solution:
    @staticmethod
    def large_group_positions_1(s: str) -> list[list[int]]:
        start, prev, result = 0, '', []

        for i, c in enumerate(s):
            if i == 0 or c == prev:
                prev = c
                continue
            if i - 1 - start > 1:
                result.append([start, i - 1])
            start = i
            prev = c

        if len(s) - 1 - start > 1:
            result.append([start, len(s) - 1])

        return result

    @staticmethod
    def large_group_positions(s: str) -> list[list[int]]:
        start, end, result = 0, 1, []

        while end <= len(s):
            *c, = s[start:end]
            if len(set(c)) == 1:
                end += 1
                continue
            if end - 2 - start > 1:
                result.append([start, end - 2])
            start = end - 1
            end += 1

        if len(s) - 1 - start > 1:
            result.append([start, len(s) - 1])

        return result


if __name__ == '__main__':
    print(Solution().large_group_positions('abbxxxxzzy'))
    assert Solution().large_group_positions('abbxxxxzzy') == [[3, 6]]
    assert Solution().large_group_positions('abc') == []
    assert Solution().large_group_positions('abcdddeeeeaabbbcd') == [[3, 5], [6, 9], [12, 14]]
    assert Solution().large_group_positions('aaa') == [[0, 2]]
    assert Solution().large_group_positions('aa') == []
