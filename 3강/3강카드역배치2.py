import sys
sys.stdin=open("input.txt", "r")

m_list = list(range(21)) #1부터 20이 쓰인 list 출력

for i in range(10):
    n, m = map(int, input().split())
    for j in range((m - n + 1) // 2):
        m_list[n + j], m_list[m - j] =  m_list[m - j], m_list[n + j]

m_list.pop(0)    
for k in m_list:    
    print(k, end = '')
