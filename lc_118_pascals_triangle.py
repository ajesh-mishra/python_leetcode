class Solution:
    @staticmethod
    def generate(numRows: int) -> list[list[int]]:
        num_rows = numRows
        result = [[1]]

        for row in range(1, num_rows + 1):
            if row == 1:
                continue

            if row == 2:
                result.append([1, 1])
                continue

            new_row = [1]

            for i in range(len(result[-1]) - 1):
                new_row.append(result[-1][i] + result[-1][i + 1])

            new_row.append(1)
            result.append(new_row)

        return result


if __name__ == "__main__":
    print(Solution().generate(5))
