import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    a, b = map(int, input().split())
    print(a + b)