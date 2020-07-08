cache = {}
def fib_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_sequence(n-1) + fib_sequence(n-2)

    return cache[n]

fib_sequence(500)
