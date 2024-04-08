class Solution:
    @staticmethod
    def min_remove_to_make_valid(s: str) -> str:
        def remove_parenthesis(string: str, left: str, right: str) -> (int, str):
            inner_running_value: int = 0
            inner_result: str = ""

            for c in string:
                match c:
                    case x if x == left:
                        inner_result += left
                        inner_running_value += 1
                    case x if x == right:
                        if (value := inner_running_value - 1) < 0:
                            continue
                        inner_running_value = value
                        inner_result += right
                    case _:
                        inner_result += c

            return inner_running_value, inner_result

        running_value, result = remove_parenthesis(s, "(", ")")

        if running_value != 0:
            _, result = remove_parenthesis(result[::-1], ")", "(")
            return result[::-1]

        return result


if __name__ == "__main__":
    assert Solution.min_remove_to_make_valid(s="lee(t(c)o)de)") == "lee(t(c)o)de"
    assert Solution.min_remove_to_make_valid(s="a)b(c)d") == "ab(c)d"
    assert Solution.min_remove_to_make_valid(s="))((") == ""
    assert Solution.min_remove_to_make_valid(s="(a(b(c)d)") == "a(b(c)d)"
