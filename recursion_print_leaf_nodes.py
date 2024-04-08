def print_leaves(adjacency_list: list[list[int]]) -> None:
    def inner(root: int) -> None:
        if len(adjacency_list) <= root:
            print(root)
            return

        for node in adjacency_list[root]:
            inner(node)

    inner(root=1)


if __name__ == "__main__":
    adjacency_list: list[list[int]] = [[], [2, 3], [4, 5], [6, 7]]
    print_leaves(adjacency_list)
