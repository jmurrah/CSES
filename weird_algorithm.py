number = int(input())

while number != 1:
    print(int(number))
    if number % 2 == 0:
        number /= 2
    else:
        number = (number * 3) + 1

print(1)