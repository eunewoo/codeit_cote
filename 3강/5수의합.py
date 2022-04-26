import sys
#sys.stdin=open("input.txt", "r")

n1 = int(input())
a1 = list(map(int, input().split()))

n2 = int(input())
a2 = list(map(int, input().split()))

d1 = 0
d2 = 0
new_list = []

while (d1 < n1 and d2 < n2):
    if a1[d1] >= a2[d2]:
        new_list.append(a2[d2])
        d2 += 1
    elif a1[d1] < a2[d2]:
        new_list.append(a1[d1])
        d1 += 1
    
if d1 == n1:
    new_list += a2[d2:n2]
elif d2 == n2:
    new_list += a1[d1:n1]

for i in new_list:
    print(i, end=' ')