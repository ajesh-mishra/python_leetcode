def binary_2_decimal(number: int) -> int:
    def inner(n: int, count) -> int:
        if n == 0:
            return 0
        return inner(n // 10, count + 1) + (2 ** (count) if n % 10 == 1 else 0)

    return inner(number, 0)


if __name__ == "__main__":
    print(binary_2_decimal(10001))
