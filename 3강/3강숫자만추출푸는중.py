import sys
sys.stdin=open("input.txt", "r")

letter = str(input())

a = [] #입력받은 문자열에서 숫자들만 뽑아서 a list 로 만들기
for i in letter.split():
    if i.isdigit():
        a.append[int(i)]

for j in range(len(a)): #a list 에서 0이 아닌 시작지점 찾기
    if a[j] != 0:
        start_index = j
        break

answer = '' #a list 속 숫자들 합치기
for k in range(start_index, len(a)):
    answer += a[k]

print(int(answer))

