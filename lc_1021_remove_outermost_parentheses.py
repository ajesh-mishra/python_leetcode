class Solution:
    @staticmethod
    def remove_outer_parentheses(s: str) -> str:
        count, temp, decompositions = 0, '', ''

        for index, char in enumerate(s):
            if char == '(':
                count += 1
            else:
                count -= 1

            temp += char
            if index != 0 and count == 0:
                decompositions += temp[1:-1]
                temp = ''

        return decompositions


if __name__ == '__main__':
    assert Solution().remove_outer_parentheses("(()())(())") == '()()()'
    assert Solution().remove_outer_parentheses("(()())(())(()(()))") == '()()()()(())'
    assert Solution().remove_outer_parentheses("()()") == ''
