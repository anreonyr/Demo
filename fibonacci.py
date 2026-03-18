def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_matrix(n: int) -> int:
    if n <= 1:
        return n

    def matrix_mult(A, B):
        return [
            [
                A[0][0] * B[0][0] + A[0][1] * B[1][0],
                A[0][0] * B[0][1] + A[0][1] * B[1][1],
            ],
            [
                A[1][0] * B[0][0] + A[1][1] * B[1][0],
                A[1][0] * B[0][1] + A[1][1] * B[1][1],
            ],
        ]

    def matrix_pow(M, power):
        result = [[1, 0], [0, 1]]
        base = M
        while power > 0:
            if power & 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            power >>= 1
        return result

    result = matrix_pow([[1, 1], [1, 0]], n)
    return result[0][1]


def main():
    n = int(input())
    print(f"计算斐波那契数列第 {n} 项:")
    print(f"递归实现:   fib({n}) = {fib_recursive(n)}")
    print(f"迭代实现:   fib({n}) = {fib_iterative(n)}")
    print(f"矩阵快速幂: fib({n}) = {fib_matrix(n)}")

    print(f"\n斐波那契数列前 {n + 1} 项 (迭代):")
    print([fib_iterative(i) for i in range(n + 1)])


if __name__ == "__main__":
    main()
