import sys
sys.stdin=open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0 for i in range(n + 2)])
a.append([0 for i in range(n + 2)])
for j in range(1, n + 1):
    a[j].insert(0, 0)
    a[j].append(0)


cnt = 0
for i in range(1 , n + 1):
    for j in range(1, n + 1):
        rep = a[i][j]
        if rep == max(a[i - 1][j], a[i][j + 1], a[i + 1][j], a[i][j - 1], a[i][j]):
            cnt += 1

print(cnt)
