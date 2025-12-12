G = int(input())
S = input().strip()
L = len(S)
g_len = L // G

res = []
for i in range(G):
    s = i * g_len
    end = s + g_len
    group = S[s:end]
    res.append(group[::-1])

print(''.join(res))