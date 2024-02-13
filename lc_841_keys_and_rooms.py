class Solution:
    def can_visit_all_rooms(self, rooms: list[list[int]]) -> bool:
        def dfs(room: int):
            if room in visited:
                return None

            visited.add(room)

            for r in rooms[room]:
                dfs(r)

        visited = set()
        dfs(0)

        return len(visited) == len(rooms)


if __name__ == "__main__":
    assert Solution().can_visit_all_rooms(rooms=[[1], [2], [3], []])
    assert not Solution().can_visit_all_rooms(rooms=[[1, 3], [3, 0, 1], [2], [0]])
