import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

sum = 0
for i in a:
    sum += i

mean = round(sum / n) #mean = ЦђБе


min = 2147000

for i in range(n):
    diff = abs(a[i] - mean)
    
    if diff < min:
        min = diff
        ans = i

    if diff == min:
        if a[i] > a[ans]:
            ans = i

print("%d %d" %(mean, ans + 1))




