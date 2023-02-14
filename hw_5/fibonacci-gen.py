ZERO = 0
ONE = 1
N = 20


def fib(n):
    num_1 = ZERO
    num_2 = ONE
    for _ in range(n):
        num_2 += num_1
        num_1 = num_2 - num_1
        yield num_1


print(fib(N))
print(*fib(N))
