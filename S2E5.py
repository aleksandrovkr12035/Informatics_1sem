raw = input().split()

for i in range(len(raw)):
    count = 0

    for j in range(len(raw)):
        if raw[i] == raw[j]:
            count += 1
    
    if count == 1:
        print(raw[i])