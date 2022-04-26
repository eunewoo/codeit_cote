import sys
#sys.stdin=open("input.txt", "r")

letter = str(input())

ans = 0 #입력받은 문자열에서 숫자들만 뽑아서 ans에다 순서대로 붙이기
for i in letter:
    if i.isdigit():
        ans = 10 * ans + int(i)

print(ans)

cnt = 1
for j in range(1, ans):
    if ans % j == 0:
        cnt += 1

print(cnt)