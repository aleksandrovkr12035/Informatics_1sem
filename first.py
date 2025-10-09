#Семинар 3.Упражнение 2

def mnogiteli(n):
    a = []
    m = 2
    
    while n > 1:
        while n % m == 0:
            a.append(m)
            n = n // m
        m += 1
    
    return a

x = int(input())
print(*mnogiteli(x))
