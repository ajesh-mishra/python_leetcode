class Solution:
    @staticmethod
    def furthest_distance_from_origin_1(moves: str) -> int:
        l_count, r_count, _count = (0, 0, 0)
        for move in moves:
            if move == 'L':
                l_count += 1
            elif move == 'R':
                r_count += 1
            else:
                _count += 1
        return abs(l_count - r_count) + _count

    @staticmethod
    def furthest_distance_from_origin(moves: str) -> int:
        l_count, r_count = moves.count('L'), moves.count('R')
        return abs(l_count - r_count) + (len(moves) - (l_count + r_count))


if __name__ == '__main__':
    # print(Solution().furthest_distance_from_origin("L_RL__R"))
    assert Solution().furthest_distance_from_origin("L_RL__R") == 3
    assert Solution().furthest_distance_from_origin("_R__LL_") == 5
    assert Solution().furthest_distance_from_origin("_______") == 7
