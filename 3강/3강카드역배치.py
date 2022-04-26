import sys
sys.stdin=open("input.txt", "r")

main_list = [] #1부터 20이 쓰인 list 출력
for i in range(1, 21):
    main_list.append(i)

for j in range(10):
    n, m=map(int, input().split())

    tmp_list = main_list[n - 1 : m] #구간추출

    tmp_list = tmp_list[::-1] #추출한구간 뒤집기

    del main_list[n - 1 : m] #구간삭제

    for k in range(len(tmp_list)): #추출한구간 재삽입
        main_list.insert(k + n - 1, tmp_list[k])
    
print(main_list)



