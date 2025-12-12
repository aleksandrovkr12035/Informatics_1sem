def deliteli(n):
    f = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    
    if n > 1:
        f.append(n)
    
    return f


x = int(input())
r = deliteli(x)
print(*r)