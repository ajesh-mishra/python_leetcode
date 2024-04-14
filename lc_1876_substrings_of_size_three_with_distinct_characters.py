class Solution:
    @staticmethod
    def count_good_substrings(s: str) -> int:
        i, j, count, sub_string = 0, 0, 0, []

        while j < len(s):
            if j - i != 3:
                sub_string.append(s[j])
                j += 1
                continue

            if len(set(sub_string)) == 3:
                count += 1

            sub_string.pop(0)
            sub_string.append(s[j])

            i += 1
            j += 1

        if len(set(sub_string)) == 3:
            count += 1

        return count


if __name__ == "__main__":
    # print(Solution.count_good_substrings(s="aababcabc"))
    assert Solution.count_good_substrings(s="xyzzaz") == 1
    assert Solution.count_good_substrings(s="aababcabc") == 4
