def print_t(size, symb, c=1):
    if c > size:
        return
    print_t(size, symb, c + 1)
    print(symb * c)

print(print_t(6, 'c'))