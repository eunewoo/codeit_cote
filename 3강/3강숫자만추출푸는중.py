import sys
sys.stdin=open("input.txt", "r")

letter = str(input())

a = [] #�Է¹��� ���ڿ����� ���ڵ鸸 �̾Ƽ� a list �� �����
for i in letter.split():
    if i.isdigit():
        a.append[int(i)]

for j in range(len(a)): #a list ���� 0�� �ƴ� �������� ã��
    if a[j] != 0:
        start_index = j
        break

answer = '' #a list �� ���ڵ� ��ġ��
for k in range(start_index, len(a)):
    answer += a[k]

print(int(answer))

