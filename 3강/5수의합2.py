#3강수들의합
import sys
sys.stdin=open("input.txt", "r")

n, m=map(int, input().split())

a = list(map(int, input().split()))

'''
cnt = 0
for i in range(n - 1):
    sum = 0
    for j in range(i, n + 1):
        sum += a[j]
        if sum == m:
            cnt += 1
            break
        elif sum > m:
            break    
'''
cnt = 0
lt = 0
rt = 0
tot = a[0]
cnt = 0


while lt < n:
    if tot >= m:
        tot -= a[lt]
        lt += 1
        rt = lt
        if tot == m:
            cnt +=1
    elif tot < m:
        if rt < n - 1:
        rt += 1

    tot += a[rt]

print(cnt)

    


