import sys
sys.stdin=open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    x, y, z =map(int, input().split())

    if y == 0:
        for j in range(z):
            ele = a[x - 1].pop(0)
            a[x - 1].append(ele)
    if y == 1:
        for j in range(z):
            ele = a[x - 1].pop()
            a[x - 1].insert(0, ele)

s = 0
e = n
sum = 0
for i in range(n):
    if i < n//2:
        for j in range(s, e):
            sum += a[i][j]
        s += 1
        e -= 1
    if i >= n//2:
        for j in range(s, e):
            sum += a[i][j]
        s -= 1
        e += 1

print(sum)

