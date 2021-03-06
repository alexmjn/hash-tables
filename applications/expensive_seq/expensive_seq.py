cache = {}


def expensive_seq(x, y, z):
    trio = (x, y, z)
    if trio in cache:
        return cache[trio]
    if x <= 0:
        cache[trio] = y + z
        return cache[trio]
    else:
        cache[trio] = (expensive_seq(x-1, y+1, z) +
                       expensive_seq(x-2, y+2, z*2) +
                       expensive_seq(x-3, y+3, z*3))

        return cache[trio]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
