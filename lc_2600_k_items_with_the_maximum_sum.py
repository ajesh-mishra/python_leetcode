class Solution:
    @staticmethod
    def k_items_with_maximum_sum(
            numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        if numOnes > k:
            return k
        elif numOnes + numZeros > k:
            return numOnes
        else:
            return (numOnes * 2) + numZeros - k


if __name__ == "__main__":
    assert (
            Solution().k_items_with_maximum_sum(numOnes=3, numZeros=2, numNegOnes=0, k=2) == 2
    )
    assert (
            Solution().k_items_with_maximum_sum(numOnes=3, numZeros=2, numNegOnes=0, k=4) == 3
    )
