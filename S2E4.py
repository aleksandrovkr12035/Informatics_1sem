#Семинар 2.Упражнение 4

raw = list(map(int, input().split()))
for i in range(0, len(raw) - 1, 2): 
    raw[i], raw[i+1] = raw[i+1], raw[i]
print(*raw)