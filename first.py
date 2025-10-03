n = 1

def print_t(size, symb, c=1):
    if c > size:
        return
    print_t(size, symb, c + 1)
    print(symb * c)
print(n)
print(print_t(6, 'c'))