class Solution:
    @staticmethod
    def make_good(s: str) -> str:
        def remove_bad(string: str, length: int) -> str:
            i, new_string = 0, ""

            while i < length:
                try:
                    if abs(ord(string[i]) - ord(string[i + 1])) == 32:
                        i += 2
                    else:
                        new_string += string[i]
                        if i + 1 == length - 1:
                            new_string += string[i + 1]
                            break
                        i += 1
                except IndexError:
                    new_string += string[i]
                    break

            if len(new_string) == length:
                return new_string

            return remove_bad(new_string, len(new_string))

        return remove_bad(s, len(s))


if __name__ == "__main__":
    assert Solution.make_good(s="leEeetcode") == "leetcode"
    assert Solution.make_good(s="abBAcC") == ""
    assert Solution.make_good(s="s") == "s"
    assert Solution.make_good(s="qFxXfQo") == "o"
