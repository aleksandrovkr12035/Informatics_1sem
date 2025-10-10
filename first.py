#Семинар 2.Упражнение 5

raw = list(map(int, input().split()))
raw = [raw[-1]] + raw[:-1]
print(*raw)
