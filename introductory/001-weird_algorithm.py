number = int(input())

while number != 1:
    print(number)
    number = int(number / 2) if number % 2 == 0 else int((number * 3) + 1)

print(1)