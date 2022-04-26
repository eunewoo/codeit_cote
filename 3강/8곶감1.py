import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

def movef(list, y, z):
    z = z % n

    if y == 0:
        rs = n - z
    elif y == 1:
        rs = z

    new_list = [0 for i in range(n)]
    for  j in range(n):
        new_list[(j + rs) % n] = list[j]

    return new_list 

for i in range(m):
    x, y, z =map(int, input().split())

    t_list = a[x - 1]

    a[x - 1] = movef(t_list, y, z)


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








