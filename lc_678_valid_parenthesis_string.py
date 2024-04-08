class Solution:
    @staticmethod
    def check_valid_string(s: str) -> bool:
        def dfs(string: str, i: int, value: int | None) -> bool:
            if value is None:
                value = 0

            value1 = value2 = value3 = value

            for index, char in enumerate(string):
                if value < 0:
                    return False
                match char:
                    case "(":
                        value += 1
                    case ")":
                        value -= 1
                    case "*":
                        value1 += dfs(string[index + 1:], i + index, value)
                        value2 += dfs(string[index + 1:], i + index, value + 1)
                        if value > 0:
                            value3 += dfs(string[index + 1:], i + index, value - 1)

            print(f"{value=}, {value1=}, {value2=}, {value3=}")

            if not has_star and value == 0:
                return True
            if not has_star and value != 0:
                return False

            if any(map(lambda x: x == 0, (value1, value2, value3))):
                return True
            else:
                return False

        has_star = s.find("*") > 0
        return dfs(s, 0, None)


if __name__ == "__main__":
    print(Solution.check_valid_string(s="()*("))
    # assert Solution.check_valid_string(s="()")
    # assert Solution.check_valid_string(s="(*)")
    # assert Solution.check_valid_string(s="(*))")
