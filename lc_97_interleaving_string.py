class Solution:
    @staticmethod
    def is_interleave(s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            dp[(i, j)] = False
            return False

        return dfs(0, 0)


if __name__ == '__main__':
    assert Solution().is_interleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
    assert Solution().is_interleave(s1="", s2="", s3="")
    assert not Solution().is_interleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
    assert not Solution().is_interleave(s1="", s2="", s3="a")
