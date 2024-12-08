n = int(input())
numbers = set(input().split())

for i in range(1, n+1):
    if str(i) not in numbers:
        print(i)
        break