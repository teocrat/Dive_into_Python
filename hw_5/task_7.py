ZERO = 0
ONE = 1
TWO = 2
N = 100


def gen_prime_num(n: int):
    for i in range(TWO, n + ONE):
        count = ZERO
        for j in range(TWO, i // TWO + ONE):
            if i % j == ZERO:
                count += ONE
        if count <= ZERO:
            yield i


print(gen_prime_num(N))
print(*gen_prime_num(N))
