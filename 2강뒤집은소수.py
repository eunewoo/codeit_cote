import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    while(x % 10 == 0):
        x = x // 10

    x = str(x)
        
    oppo_num = ''
    for j in x:
        oppo_num = j + oppo_num

    oppo_num = int(oppo_num)
    return oppo_num

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
   
    return True

b = []
for i in range(len(a)):
    new_a = reverse(a[i])
    a[i] = new_a
    if isPrime(a[i]):
        b.append(a[i])

print(*b)


    


