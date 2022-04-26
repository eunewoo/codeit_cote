import sys
sys.stdin=open("input.txt", "r")

n = int(input())

for i in range(n):
    tmp = str(input()).lower()
    tmp_len = len(tmp)
    for j in range (tmp_len // 2):
        if tmp[j] != tmp[tmp_len - 1 - j]:
            print("#%d %s" %(i + 1, "NO"))
            break
    else:
        print("#%d %s" %(i + 1, "YES"))     



