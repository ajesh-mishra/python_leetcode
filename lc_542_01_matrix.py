import collections


class Solution:
    @staticmethod
    def update_matrix(mat: list[list[int]]) -> list[list[int]]:
        length = len(mat)
        width = len(mat[0])

        visited = [[False for _ in range(width)] for _ in range(length)]
        queue = collections.deque()

        for i in range(length):
            for j in range(width):
                if mat[i][j] != 0:
                    continue
                visited[i][j] = True
                queue.append((i, j, 0))

        while queue:
            i, j, distance = queue.popleft()
            for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i = i + delta_i
                new_j = j + delta_j
                if not 0 <= new_i < length \
                        or not 0 <= new_j < width \
                        or visited[new_i][new_j]:
                    continue
                visited[new_i][new_j] = True
                mat[new_i][new_j] = distance + 1
                queue.append((new_i, new_j, distance + 1))

        return mat


if __name__ == '__main__':
    print(Solution().update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(Solution().update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
