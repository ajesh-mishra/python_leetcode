class Solution:
    @staticmethod
    def exist(board: list[list[str]], word: str) -> bool:
        m: int = len(board)
        n: int = len(board[0])
        word_length = len(word)

        def dfs(a: int, b: int, index: int) -> bool:
            if word_length == index:
                return True

            visited[a][b] = True

            for new_a, new_b in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
                if not 0 <= new_a < m or not 0 <= new_b < n:
                    continue
                if visited[new_a][new_b]:
                    continue
                if board[new_a][new_b] != word[index]:
                    continue

                if dfs(new_a, new_b, index + 1):
                    return True
                else:
                    visited[new_a][new_b] = False

        for x, y in [(i, j) for i in range(m) for j in range(n)]:
            if board[x][y] != word[0]:
                continue

            visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(m)]
            visited[x][y] = True

            if dfs(x, y, 1):
                return True

        return False


if __name__ == "__main__":
    assert Solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        word="ABCESEEEFS",
    )
    assert Solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
    assert Solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
    assert not Solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
