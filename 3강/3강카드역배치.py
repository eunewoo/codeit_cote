import sys
sys.stdin=open("input.txt", "r")

main_list = [] #1���� 20�� ���� list ���
for i in range(1, 21):
    main_list.append(i)

for j in range(10):
    n, m=map(int, input().split())

    tmp_list = main_list[n - 1 : m] #��������

    tmp_list = tmp_list[::-1] #�����ѱ��� ������

    del main_list[n - 1 : m] #��������

    for k in range(len(tmp_list)): #�����ѱ��� �����
        main_list.insert(k + n - 1, tmp_list[k])
    
print(main_list)



