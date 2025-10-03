#Упражнение 1. Карты

n = int(input())
numbers = list(map(int, input().split()))

total = 0
sum = 0

for i in range(1, n + 1):
    sum += i

for i in numbers:
    total += i

print (sum - total)