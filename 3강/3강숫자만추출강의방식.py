import sys
#sys.stdin=open("input.txt", "r")

letter = str(input())

ans = 0 #�Է¹��� ���ڿ����� ���ڵ鸸 �̾Ƽ� ans���� ������� ���̱�
for i in letter:
    if i.isdigit():
        ans = 10 * ans + int(i)

print(ans)

cnt = 1
for j in range(1, ans):
    if ans % j == 0:
        cnt += 1

print(cnt)