import sys
sys.stdin=open("input.txt", "r")

def palindrome(word):
    palin = ""
    for i in range(len(word)):
        palin =  palin + word[len(word) -1 - i] 
    return palin

w_range = int(input())
for j in range(1, w_range + 1):
    n = str(input())
    if n.upper() == palindrome(n).upper():
        print("#%d YES" %(j))
    else:
        print("#%d NO" %(j))
