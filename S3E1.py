def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


N = int(input("Введи, быстро, не думай,  номер числа Фибоначчи: "))
print(fibonacci(N))