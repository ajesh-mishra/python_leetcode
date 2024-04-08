def decimal_2_binary(number: int) -> str:
    def inner(n: int) -> str:
        if n == 0:
            return ""
        return inner(n // 2) + str(n % 2)

    return inner(number)


if __name__ == "__main__":
    assert decimal_2_binary(4) == "100"
    assert decimal_2_binary(233) == "11101001"
