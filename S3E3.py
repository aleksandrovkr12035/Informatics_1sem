def G(a, b):
    if b == 0:
        return [a, 1, 0]
    res = G(b, a % b)
    s = res[2]
    res[2] = res[1] - (a // b) * res[2]
    res[1] = s
    return res


a, b = map(int, input().split())
g, x, y = G(a, b)
print(x,y,g)